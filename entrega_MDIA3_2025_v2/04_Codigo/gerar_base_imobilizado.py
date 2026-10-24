#!/usr/bin/env python3
"""Gera a versão 2.0 de uma população didática, inteiramente sintética, de 500.000 itens de imobilizado.

A população NÃO contém registros reais da M. Dias Branco. Somente os totais agregados
por classe foram calibrados para reconciliar com a Nota 11 das DFs consolidadas de 2025.
"""
from __future__ import annotations
import argparse
import csv
import gzip
import json
from pathlib import Path
from typing import Dict, List, Tuple
import numpy as np

SEED_DEFAULT = 20261021
AS_OF = "2025-12-31"
# Saldos publicados na Nota 11, em BRL mil. A geração trabalha em reais inteiros,
# preservando o valor divulgado a três casas decimais de BRL mil (BRL 1).
CLASSES = [
    {"nome": "Edificações", "n": 3_000, "custo_mil": 1_740_776, "dep_mil": 548_812,
     "subtipos": ["edificação fabril", "armazém", "edifício administrativo"]},
    {"nome": "Máquinas e equipamentos", "n": 210_000, "custo_mil": 3_682_384, "dep_mil": 2_388_537,
     "subtipos": ["máquina de produção", "equipamento de processo", "linha de embalagem", "equipamento auxiliar"]},
    {"nome": "Móveis e utensílios", "n": 160_000, "custo_mil": 145_342, "dep_mil": 97_227,
     "subtipos": ["móvel de escritório", "utensílio fabril", "equipamento de apoio"]},
    {"nome": "Veículos", "n": 10_000, "custo_mil": 256_948, "dep_mil": 127_743,
     "subtipos": ["veículo de carga", "veículo de apoio", "equipamento móvel"]},
    {"nome": "Instalações", "n": 40_000, "custo_mil": 572_492, "dep_mil": 306_773,
     "subtipos": ["instalação elétrica", "instalação industrial", "sistema de utilidades"]},
    {"nome": "Imobilizações em andamento", "n": 30_000, "custo_mil": 415_229, "dep_mil": 2_220,
     "subtipos": ["projeto fabril em andamento", "montagem em andamento", "obra em andamento"]},
    {"nome": "Outros", "n": 47_000, "custo_mil": 392_524, "dep_mil": 163_393,
     "subtipos": ["benfeitoria", "equipamento de informática", "instalação diversa", "outro item de imobilizado"]},
]
assert sum(c["n"] for c in CLASSES) == 500_000

# Cinco bens fictícios baixados, mas ainda registrados, com exposição potencial agregada
# de BRL 39.000 mil (BRL 39 milhões). Esses registros são erros deliberadamente inseridos.
DISPOSAL_EXCEPTIONS = [
    (14_000_000, 2_000_000),
    (12_500_000, 2_500_000),
    (10_000_000, 2_000_000),
    (7_000_000, 2_000_000),
    (5_000_000, 1_000_000),
]


def allocate_positive(total: int, n: int, rng: np.random.Generator) -> np.ndarray:
    """Distribui total inteiro em n itens positivos, com soma exata."""
    if n <= 0 or total < n:
        raise ValueError(f"Alocação positiva inválida: total={total}, n={n}")
    weights = rng.lognormal(mean=0.0, sigma=1.05, size=n)
    remaining = total - n
    raw = remaining * weights / weights.sum()
    base = np.floor(raw).astype(np.int64)
    left = int(remaining - int(base.sum()))
    if left:
        frac = raw - base
        pick = np.argpartition(frac, -left)[-left:]
        base[pick] += 1
    out = base + 1
    assert int(out.sum()) == total and int(out.min()) >= 1
    return out


def allocate_capped(total: int, weights: np.ndarray, caps: np.ndarray) -> np.ndarray:
    """Aloca um total inteiro com soma exata sem exceder a capacidade de cada item."""
    weights = np.asarray(weights, dtype=np.float64)
    caps = np.asarray(caps, dtype=np.int64)
    if total < 0 or total > int(caps.sum()):
        raise ValueError("Total fora da capacidade disponível")
    out = np.zeros(len(caps), dtype=np.int64)
    remaining = int(total)
    for _ in range(100):
        if remaining == 0:
            break
        eligible = np.flatnonzero(out < caps)
        if not len(eligible):
            raise RuntimeError("Sem capacidade para fechar a alocação")
        w = weights[eligible].copy()
        w[w <= 0] = 1e-12
        raw = remaining * w / w.sum()
        whole = np.floor(raw).astype(np.int64)
        room = caps[eligible] - out[eligible]
        add = np.minimum(whole, room)
        got = int(add.sum())
        if got:
            out[eligible] += add
            remaining -= got
        if remaining == 0:
            break
        eligible = np.flatnonzero(out < caps)
        if not len(eligible):
            raise RuntimeError("Sem capacidade para fechar a alocação")
        if got == 0:
            # Quando restam poucas unidades, atribui-as por maiores pesos.
            k = min(remaining, len(eligible))
            order = eligible[np.argpartition(weights[eligible], -k)[-k:]]
            out[order] += 1
            remaining -= k
        else:
            # O passo de maiores restos fecha arredondamentos sem exceder caps.
            k = min(remaining, len(eligible))
            local_raw = raw
            frac = local_raw - whole
            # candidatos podem ter sido limitados por cap; usa frações mais pesos para desempate.
            ranking = frac + (w / w.max()) * 1e-12
            candidates = eligible[np.argpartition(ranking, -k)[-k:]]
            candidates = candidates[out[candidates] < caps[candidates]]
            if len(candidates):
                k2 = min(remaining, len(candidates))
                if k2 < len(candidates):
                    candidates = candidates[np.argpartition(weights[candidates], -k2)[-k2:]]
                out[candidates[:k2]] += 1
                remaining -= k2
    if remaining:
        # Fallback seguro e determinístico, normalmente não necessário.
        eligible = np.flatnonzero(out < caps)
        for i in eligible:
            add = min(remaining, int(caps[i] - out[i]))
            out[i] += add
            remaining -= add
            if not remaining:
                break
    if remaining or int(out.sum()) != total or np.any(out > caps):
        raise RuntimeError("Falha de reconciliação na alocação limitada")
    return out


def money_k_from_reais(value: int) -> str:
    """Formata BRL mil com três casas (R$ 1 de precisão) e vírgula decimal."""
    value = int(value)
    return f"{value // 1000},{value % 1000:03d}"


def date_for_row(rng: np.random.Generator, start: str = "1990-01-01", end: str = AS_OF) -> str:
    a = np.datetime64(start, "D").astype("int64")
    b = np.datetime64(end, "D").astype("int64")
    day = int(rng.integers(a, b + 1))
    return str(np.datetime64(day, "D"))


def generate(out_dir: Path, seed: int = SEED_DEFAULT) -> dict:
    out_dir.mkdir(parents=True, exist_ok=True)
    rng = np.random.default_rng(seed)
    output_csv = out_dir / "base_imobilizado_sintetica_500000.csv.gz"
    truth_path = out_dir / "registro_excecoes_inseridas.csv"
    summary_path = out_dir / "parametros_e_reconciliacao_base.json"
    population_rows = 0
    next_id = 1
    class_summary = []
    truth_rows: List[Tuple[str, str, str, str, str]] = []
    plant_numbers: Dict[str, List[str]] = {}
    plant_index = 0

    header = [
        "asset_id_sintetico", "registro_sintetico", "classe_contabil", "subtipo_sintetico",
        "unidade_ficticia", "data_capitalizacao_sintetica", "data_disponivel_uso_sintetica",
        "status_operacional_sintetico", "data_baixa_sintetica", "etiqueta_fisica_sintetica",
        "resultado_vistoria_sintetica", "custo_historico_R$_mil",
        "depreciacao_acumulada_R$_mil", "valor_contabil_liquido_R$_mil"
    ]

    with gzip.open(output_csv, "wt", encoding="utf-8-sig", newline="", compresslevel=9) as f:
        writer = csv.writer(f, delimiter=";", lineterminator="\n")
        writer.writerow(header)
        for spec in CLASSES:
            n = spec["n"]
            target_cost = int(spec["custo_mil"] * 1000)
            target_dep = int(spec["dep_mil"] * 1000)
            costs = np.zeros(n, dtype=np.int64)
            deps = np.zeros(n, dtype=np.int64)
            pins = []
            if spec["nome"] == "Máquinas e equipamentos":
                pins = list(range(len(DISPOSAL_EXCEPTIONS)))
                pinned_cost = sum(a for a, _ in DISPOSAL_EXCEPTIONS)
                pinned_dep = sum(b for _, b in DISPOSAL_EXCEPTIONS)
                costs[pins] = [a for a, _ in DISPOSAL_EXCEPTIONS]
                deps[pins] = [b for _, b in DISPOSAL_EXCEPTIONS]
                costs[5:] = allocate_positive(target_cost - pinned_cost, n - len(pins), rng)
                remaining_dep = target_dep - pinned_dep
                target_ratio = remaining_dep / max(1, int(costs[5:].sum()))
                alpha = max(0.15, target_ratio * 28)
                beta = max(0.15, (1 - target_ratio) * 28)
                rates = rng.beta(alpha, beta, size=n - len(pins))
                dep_weights = costs[5:].astype(np.float64) * np.maximum(rates, 1e-6)
                deps[5:] = allocate_capped(remaining_dep, dep_weights, costs[5:])
            else:
                costs = allocate_positive(target_cost, n, rng)
                if target_dep:
                    target_ratio = target_dep / target_cost
                    alpha = max(0.15, target_ratio * 28)
                    beta = max(0.15, (1 - target_ratio) * 28)
                    rates = rng.beta(alpha, beta, size=n)
                    dep_weights = costs.astype(np.float64) * np.maximum(rates, 1e-6)
                    deps = allocate_capped(target_dep, dep_weights, costs)
            nbv = costs - deps
            if int(costs.sum()) != target_cost or int(deps.sum()) != target_dep or int(nbv.sum()) != target_cost-target_dep:
                raise AssertionError(f"Falha de conciliação na classe {spec['nome']}")

            ids = [f"SIM-IMOB-{i:06d}" for i in range(next_id, next_id + n)]
            next_id += n
            start_pos = population_rows
            local_positions = np.arange(n)
            subtypes = rng.choice(spec["subtipos"], size=n)
            plants = [f"UNIDADE-SIM-{int(x):02d}" for x in rng.integers(1, 9, size=n)]
            acquisition_dates = [date_for_row(rng) for _ in range(n)]
            available_dates = [""] * n
            statuses = ["Em uso" if spec["nome"] != "Imobilizações em andamento" else "Em andamento" for _ in range(n)]
            disposal_dates = [""] * n
            tags = [f"TAG-SIM-{i:06d}" for i in range(next_id - n, next_id)]
            physical = ["Não selecionado" for _ in range(n)]
            # Datas são metadados fictícios e não determinam a alocação de depreciação.
            # Para preservar coerência temporal, os cinco itens baixados antecedem a baixa,
            # e os 12 projetos sinalizados antecedem a data sintética de disponibilidade.
            if spec["nome"] == "Máquinas e equipamentos":
                for j in range(len(DISPOSAL_EXCEPTIONS)):
                    acquisition_dates[j] = date_for_row(rng, "2010-01-01", "2024-12-31")
            if spec["nome"] == "Imobilizações em andamento":
                for j in range(min(12, n)):
                    acquisition_dates[j] = date_for_row(rng, "2010-01-01", "2024-12-31")
                    available_dates[j] = "2025-01-01"

            # Exceções observáveis, todas plantadas apenas para a simulação didática.
            if spec["nome"] == "Máquinas e equipamentos":
                for j in pins:
                    statuses[j] = "Baixado antes do encerramento, mantido no registro"
                    disposal_dates[j] = "2025-12-15"
                    truth_rows.append((ids[j], "BAIXA_NAO_REGISTRADA", "Bem baixado antes do encerramento ainda consta no cadastro e mantém valor contábil", money_k_from_reais(int(nbv[j])), "Potencial superavaliação; exposição potencial igual ao valor contábil"))
            if spec["nome"] == "Imobilizações em andamento":
                for j in range(min(12, n)):
                    truth_rows.append((ids[j], "CIP_DISPONIVEL_NAO_TRANSFERIDO", "Projeto com data de disponibilidade sintética e status ainda em andamento", "", "Sinal qualitativo de classificação; não quantificado, e a data não é evidência nem insumo do rateio sintético de depreciação"))
            if spec["nome"] == "Móveis e utensílios":
                for j in range(12):
                    tags[j] = ""
                    truth_rows.append((ids[j], "ETIQUETA_AUSENTE", "Registro sem etiqueta física sintética", "", "Exceção de rastreabilidade; não quantificada sem inspeção/prova de existência"))
                for j in range(12, 20):
                    physical[j] = "Não localizado no cenário sintético"
                    truth_rows.append((ids[j], "NAO_LOCALIZADO_SIMULADO", "Registro não localizado no resultado de vistoria puramente sintético", money_k_from_reais(int(nbv[j])), "Possível exposição de existência; não constitui evidência real"))

            for j in range(n):
                writer.writerow([
                    ids[j], "SIM — POPULAÇÃO SINTÉTICA", spec["nome"], subtypes[j], plants[j],
                    acquisition_dates[j], available_dates[j], statuses[j], disposal_dates[j],
                    tags[j], physical[j], money_k_from_reais(int(costs[j])),
                    money_k_from_reais(int(deps[j])), money_k_from_reais(int(nbv[j]))
                ])
            population_rows += n
            class_summary.append({
                "classe_contabil": spec["nome"], "linhas_sinteticas": n,
                "custo_publicado_R$_mil": spec["custo_mil"], "custo_gerado_R$_mil": int(costs.sum()) // 1000,
                "depreciacao_publicada_R$_mil": spec["dep_mil"], "depreciacao_gerada_R$_mil": int(deps.sum()) // 1000,
                "saldo_liquido_publicado_R$_mil": spec["custo_mil"] - spec["dep_mil"],
                "saldo_liquido_gerado_R$_mil": int(nbv.sum()) // 1000,
            })

    with truth_path.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.writer(f, delimiter=";", lineterminator="\n")
        writer.writerow(["asset_id_sintetico", "codigo_excecao_inserida", "descricao_cenario", "exposicao_potencial_R$_mil", "natureza_e_limitacao"])
        writer.writerows(truth_rows)

    totals = {
        "matricula": "202062044",
        "base": output_csv.name,
        "seed": seed,
        "data_referencia": AS_OF,
        "registros_de_dados": population_rows,
        "linhas_com_cabecalho_no_csv_descompactado": population_rows + 1,
        "unidade_monetaria": "BRL mil, 3 casas decimais (BRL 1 de precisão)",
        "aviso": "População integralmente sintética. IDs, classes por item, datas, unidades, subtipo, etiquetas, vistoria e rateio individual de custos/depreciação não são dados da MDIA3. Datas não são insumo do rateio sintético de depreciação. Somente saldos agregados por classe foram calibrados à Nota 11 consolidada de 2025.",
        "versao_metodo": "2.0 — removidas vidas úteis/taxas/métodos por item sem evidência de cadastro; nenhuma depreciação individual é inferida a partir das datas sintéticas.",
        "totais_publicados_R$_mil": {
            "custo_historico": sum(c["custo_mil"] for c in CLASSES),
            "depreciacao_acumulada": sum(c["dep_mil"] for c in CLASSES),
            "valor_contabil_liquido": sum(c["custo_mil"]-c["dep_mil"] for c in CLASSES),
        },
        "totais_gerados_R$_mil": {
            "custo_historico": sum(x["custo_gerado_R$_mil"] for x in class_summary),
            "depreciacao_acumulada": sum(x["depreciacao_gerada_R$_mil"] for x in class_summary),
            "valor_contabil_liquido": sum(x["saldo_liquido_gerado_R$_mil"] for x in class_summary),
        },
        "classes": class_summary,
        "registro_de_excecoes_inseridas": truth_path.name,
        "quantidade_de_excecoes_inseridas": len(truth_rows),
        "fundamento_sintetico": "CPC 27, item 9, exige julgamento sobre a unidade de reconhecimento. O cenário assume um item fictício por linha; não replica a política contábil nem o auxiliar patrimonial da companhia. O custo e a depreciação por item são rateios sintéticos usados para conciliar os totais divulgados por classe.",
    }
    summary_path.write_text(json.dumps(totals, ensure_ascii=False, indent=2), encoding="utf-8")
    if population_rows != 500_000:
        raise AssertionError(f"Esperados 500.000 registros; gerados {population_rows}")
    if totals["totais_gerados_R$_mil"] != totals["totais_publicados_R$_mil"]:
        raise AssertionError("A população sintética não conciliou com os saldos publicados")
    return totals


def main() -> None:
    parser = argparse.ArgumentParser(description="Gera 500.000 itens sintéticos de imobilizado e reconcilia a Nota 11")
    parser.add_argument("--output-dir", default=".", help="Pasta de saída")
    parser.add_argument("--seed", type=int, default=SEED_DEFAULT, help="Semente determinística")
    args = parser.parse_args()
    result = generate(Path(args.output_dir), args.seed)
    print(json.dumps({"arquivo": result["base"], "registros": result["registros_de_dados"], "totais": result["totais_gerados_R$_mil"], "excecoes_inseridas": result["quantidade_de_excecoes_inseridas"]}, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()
