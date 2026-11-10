#!/usr/bin/env python3
"""Executa procedimentos didáticos sobre a população sintética de imobilizado.

O script NÃO lê razão contábil da companhia nem produz evidência de auditoria real.
A seleção e as exceções são unicamente do cenário didático descrito nos arquivos.
"""
from __future__ import annotations
import argparse
import csv
import gzip
import heapq
import json
import math
from collections import defaultdict
from decimal import Decimal
from pathlib import Path
import numpy as np

SEED_SAMPLE = 5302025
N_POP = 500_000
MATERIALIDADE_GLOBAL_R_MIL = Decimal("35413.500")
MATERIALIDADE_EXECUCAO_R_MIL = Decimal("17706.750")
LIMIAR_TRIVIAL_R_MIL = Decimal("1770.675")
MUS_CONFIANCE_FACTOR = Decimal("3.0")


def dec_k(s: str) -> Decimal:
    if s is None or s.strip() == "":
        return Decimal("0")
    return Decimal(s.strip().replace(".", "").replace(",", "."))


def write_csv(path: Path, fieldnames, rows) -> None:
    with path.open("w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames, delimiter=";", lineterminator="\n", extrasaction="ignore")
        w.writeheader()
        for row in rows:
            formatted = {k: (format(v, "f").replace(".", ",") if isinstance(v, Decimal) else v) for k, v in row.items()}
            w.writerow(formatted)


def main() -> None:
    ap = argparse.ArgumentParser(description="Testes didáticos da base de imobilizado sintética")
    ap.add_argument("--base", default="base_imobilizado_sintetica_500000.csv.gz")
    ap.add_argument("--out-dir", default=".")
    ap.add_argument("--truth", default=None, help="CSV da lista-verdade; por padrão, procura junto à base e depois em --out-dir")
    ap.add_argument("--seed", type=int, default=SEED_SAMPLE)
    args = ap.parse_args()
    base_path = Path(args.base)
    out = Path(args.out_dir)
    out.mkdir(parents=True, exist_ok=True)

    if not base_path.exists():
        raise FileNotFoundError(base_path)
    rng = np.random.default_rng(args.seed)
    random_indices = set(int(x) for x in rng.choice(N_POP, size=384, replace=False))
    class_totals = defaultdict(lambda: {"n": 0, "custo": Decimal(0), "dep": Decimal(0), "nbv": Decimal(0)})
    detected = defaultdict(list)
    exceptions_rows = []
    random_sample = []
    sample_by_id = {}
    top_heap = []
    seen = set()
    population_count = 0
    sum_cost = Decimal(0)
    sum_dep = Decimal(0)
    sum_nbv = Decimal(0)
    mismatch_count = 0
    dep_exceeds_cost_count = 0
    fieldnames = None

    with gzip.open(base_path, "rt", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f, delimiter=";")
        fieldnames = reader.fieldnames
        required = {"asset_id_sintetico", "classe_contabil", "data_disponivel_uso_sintetica", "status_operacional_sintetico", "etiqueta_fisica_sintetica", "resultado_vistoria_sintetica", "custo_historico_R$_mil", "depreciacao_acumulada_R$_mil", "valor_contabil_liquido_R$_mil"}
        if not required.issubset(set(fieldnames or [])):
            raise ValueError("A base não contém todas as colunas necessárias")
        for idx, row in enumerate(reader):
            population_count += 1
            asset_id = row["asset_id_sintetico"]
            if asset_id in seen:
                raise AssertionError(f"ID duplicado: {asset_id}")
            seen.add(asset_id)
            cls = row["classe_contabil"]
            cost = dec_k(row["custo_historico_R$_mil"])
            dep = dec_k(row["depreciacao_acumulada_R$_mil"])
            nbv = dec_k(row["valor_contabil_liquido_R$_mil"])
            sum_cost += cost
            sum_dep += dep
            sum_nbv += nbv
            class_totals[cls]["n"] += 1
            class_totals[cls]["custo"] += cost
            class_totals[cls]["dep"] += dep
            class_totals[cls]["nbv"] += nbv
            if (cost - dep) != nbv:
                mismatch_count += 1
            if dep > cost:
                dep_exceeds_cost_count += 1

            flags = []
            status = row["status_operacional_sintetico"]
            ready = row["data_disponivel_uso_sintetica"]
            physical = row["resultado_vistoria_sintetica"]
            tag = row["etiqueta_fisica_sintetica"]
            if status.startswith("Baixado antes do encerramento") and nbv > 0:
                flags.append("BAIXA_NAO_REGISTRADA")
                detected["BAIXA_NAO_REGISTRADA"].append(asset_id)
                exceptions_rows.append({"asset_id_sintetico": asset_id, "codigo_teste": "BAIXA_NAO_REGISTRADA", "classe": cls, "valor_contabil_R$_mil": nbv, "exposicao_potencial_R$_mil": nbv, "avaliacao": "Potencial superavaliação; a existência e o efeito dependeriam de evidência real"})
            if cls == "Imobilizações em andamento" and ready and ready <= "2025-12-31" and status == "Em andamento":
                flags.append("CIP_DISPONIVEL_NAO_TRANSFERIDO")
                detected["CIP_DISPONIVEL_NAO_TRANSFERIDO"].append(asset_id)
                exceptions_rows.append({"asset_id_sintetico": asset_id, "codigo_teste": "CIP_DISPONIVEL_NAO_TRANSFERIDO", "classe": cls, "valor_contabil_R$_mil": nbv, "exposicao_potencial_R$_mil": "Não quantificada", "avaliacao": "Possível erro de classificação/depreciação; quantificação depende de evidência da disponibilidade, vida útil e valor residual"})
            if not tag:
                flags.append("ETIQUETA_AUSENTE")
                detected["ETIQUETA_AUSENTE"].append(asset_id)
                exceptions_rows.append({"asset_id_sintetico": asset_id, "codigo_teste": "ETIQUETA_AUSENTE", "classe": cls, "valor_contabil_R$_mil": nbv, "exposicao_potencial_R$_mil": "Não quantificada", "avaliacao": "Deficiência de rastreabilidade sintética; não é, isoladamente, distorção contábil"})
            if physical == "Não localizado no cenário sintético":
                flags.append("NAO_LOCALIZADO_SIMULADO")
                detected["NAO_LOCALIZADO_SIMULADO"].append(asset_id)
                exceptions_rows.append({"asset_id_sintetico": asset_id, "codigo_teste": "NAO_LOCALIZADO_SIMULADO", "classe": cls, "valor_contabil_R$_mil": nbv, "exposicao_potencial_R$_mil": nbv, "avaliacao": "Sinal de risco de existência inteiramente simulado; exige inspeção/documentação real antes de qualquer conclusão"})

            sample_record = dict(row)
            sample_record["flags_teste_populacao"] = " | ".join(flags)
            if idx in random_indices:
                sample_record["origem_selecao"] = "AAS aleatória simples, sem reposição (n=384)"
                random_sample.append(sample_record)
                sample_by_id[asset_id] = sample_record
            if flags:
                if asset_id in sample_by_id:
                    sample_by_id[asset_id]["origem_selecao"] += " + seleção dirigida por exceção"
                    sample_by_id[asset_id]["flags_teste_populacao"] = " | ".join(flags)
                else:
                    sample_record["origem_selecao"] = "Censo de regra de exceção"
                    sample_by_id[asset_id] = sample_record

            # Mantém os 25 maiores saldos para seleção individual focada; não projetável.
            item = (nbv, idx, asset_id, sample_record)
            if len(top_heap) < 25:
                heapq.heappush(top_heap, item)
            elif item[0] > top_heap[0][0]:
                heapq.heapreplace(top_heap, item)

    if population_count != N_POP:
        raise AssertionError(f"Esperados {N_POP} registros, encontrados {population_count}")

    # Adiciona os 25 maiores itens a teste focado, preservando a identificação da seleção.
    for _, _, asset_id, record in top_heap:
        if asset_id in sample_by_id:
            if "top 25" not in sample_by_id[asset_id]["origem_selecao"]:
                sample_by_id[asset_id]["origem_selecao"] += " + top 25 saldos"
        else:
            copy = dict(record)
            copy["origem_selecao"] = "Seleção dirigida: top 25 saldos (não projetável)"
            sample_by_id[asset_id] = copy

    # AAS descritiva de qualidade da base sintética: presença dos campos-chave.
    # Não é teste de controle da companhia nem amostra de auditoria sobre dados reais.
    aas_required_fields = ["asset_id_sintetico", "classe_contabil", "custo_historico_R$_mil", "depreciacao_acumulada_R$_mil", "valor_contabil_liquido_R$_mil"]
    aas_rows_with_missing = sum(1 for row in random_sample if any(not row.get(field, "").strip() for field in aas_required_fields))

    # A lista-verdade pertence ao conjunto da base; --out-dir pode ser independente.
    truth_candidates = [Path(args.truth)] if args.truth else [
        base_path.parent / "registro_excecoes_inseridas.csv",
        out / "registro_excecoes_inseridas.csv",
    ]
    truth_path = next((path for path in truth_candidates if path.is_file()), None)
    if truth_path is None:
        expected = args.truth or "registro_excecoes_inseridas.csv junto à base ou em --out-dir"
        raise FileNotFoundError(f"Lista-verdade ausente: {expected}. Informe --truth para comparar exceções inseridas e identificadas.")
    truth = defaultdict(set)
    with truth_path.open("r", encoding="utf-8-sig", newline="") as f:
        for row in csv.DictReader(f, delimiter=";"):
            truth[row["codigo_excecao_inserida"]].add(row["asset_id_sintetico"])
    comparison = []
    for code in sorted(set(truth) | set(detected)):
        expected = truth.get(code, set())
        found = set(detected.get(code, []))
        comparison.append({
            "codigo_excecao": code,
            "itens_inseridos": len(expected),
            "itens_identificados": len(found),
            "verdadeiros_positivos": len(expected & found),
            "nao_identificados": len(expected - found),
            "falsos_positivos": len(found - expected),
            "resultado": "Concordante no cenário sintético" if expected == found else "Divergência a investigar"
        })

    sample_fields = list(fieldnames or []) + ["origem_selecao", "flags_teste_populacao"]
    combined = sorted(sample_by_id.values(), key=lambda r: r["asset_id_sintetico"])
    write_csv(out / "amostra_combinada_auditoria.csv", sample_fields, combined)
    write_csv(out / "amostra_aleatoria_384.csv", sample_fields, random_sample)
    write_csv(out / "excecoes_identificadas_testes.csv", ["asset_id_sintetico", "codigo_teste", "classe", "valor_contabil_R$_mil", "exposicao_potencial_R$_mil", "avaliacao"], exceptions_rows)
    write_csv(out / "comparacao_excecoes_inseridas_identificadas.csv", ["codigo_excecao", "itens_inseridos", "itens_identificados", "verdadeiros_positivos", "nao_identificados", "falsos_positivos", "resultado"], comparison)

    class_rows = []
    for cls, vals in class_totals.items():
        class_rows.append({"classe_contabil": cls, "linhas": vals["n"], "custo_historico_R$_mil": vals["custo"], "depreciacao_acumulada_R$_mil": vals["dep"], "saldo_liquido_R$_mil": vals["nbv"]})
    write_csv(out / "conciliacao_por_classe_base.csv", ["classe_contabil", "linhas", "custo_historico_R$_mil", "depreciacao_acumulada_R$_mil", "saldo_liquido_R$_mil"], class_rows)

    # MUS sistemática com início aleatório. Fator 3,0 equivale à hipótese didática
    # de 95% de confiança e erro esperado zero; não substitui julgamento de auditor.
    mus_n = math.ceil(MUS_CONFIANCE_FACTOR * sum_nbv / MATERIALIDADE_EXECUCAO_R_MIL)
    mus_interval = sum_nbv / Decimal(mus_n)
    mus_rng = np.random.default_rng(args.seed + 1)
    mus_start = Decimal(str(mus_rng.uniform(0, float(mus_interval))))
    mus_rows = {}
    cumulative = Decimal(0)
    threshold_idx = 0
    with gzip.open(base_path, "rt", encoding="utf-8-sig", newline="") as f:
        for row in csv.DictReader(f, delimiter=";"):
            nbv = dec_k(row["valor_contabil_liquido_R$_mil"])
            previous = cumulative
            cumulative += nbv
            while threshold_idx < mus_n and mus_start + mus_interval * threshold_idx < cumulative:
                if mus_start + mus_interval * threshold_idx >= previous:
                    asset_id = row["asset_id_sintetico"]
                    record = mus_rows.setdefault(
                        asset_id,
                        {
                            **row,
                            "ordem_selecao_mus": threshold_idx + 1,
                            "unidades_monetarias_selecionadas": 0,
                            "ordens_selecao_mus": [],
                        },
                    )
                    record["unidades_monetarias_selecionadas"] += 1
                    record["ordens_selecao_mus"].append(threshold_idx + 1)
                threshold_idx += 1
    if threshold_idx != mus_n:
        raise AssertionError(f"Esperadas {mus_n} seleções monetárias; concluídas {threshold_idx}")
    mus_output = sorted(mus_rows.values(), key=lambda r: r["ordem_selecao_mus"])
    mus_ids = set(mus_rows)
    mus_disposals = len(mus_ids & set(detected.get("BAIXA_NAO_REGISTRADA", [])))
    mus_fields = list(fieldnames or []) + [
        "ordem_selecao_mus",
        "unidades_monetarias_selecionadas",
        "ordens_selecao_mus",
    ]
    write_csv(out / "amostra_monetaria_MUS.csv", mus_fields, mus_output)

    disp = [x for x in exceptions_rows if x["codigo_teste"] == "BAIXA_NAO_REGISTRADA"]
    disp_exposure = sum((Decimal(x["exposicao_potencial_R$_mil"]) for x in disp), Decimal(0))
    selected_disposals = set(detected.get("BAIXA_NAO_REGISTRADA", [])) & set(mus_rows)
    mus_certainty_error = Decimal(0)
    mus_noncertainty_count = 0
    mus_point_projection = Decimal(0)
    mus_projection_details = []
    for asset_id in sorted(
        selected_disposals,
        key=lambda x: mus_rows[x]["ordem_selecao_mus"],
    ):
        record = mus_rows[asset_id]
        book_value = dec_k(record["valor_contabil_liquido_R$_mil"])
        # A condição de distorção de 100% é premissa do cenário de baixa sem contraprestação.
        # Itens de certeza entram pelo erro observado; os demais, por intervalo × tainting.
        certainty = (
            book_value >= mus_interval
            or int(record["unidades_monetarias_selecionadas"]) > 1
        )
        tainting = (book_value / book_value) if book_value else Decimal(0)
        if certainty:
            mus_certainty_error += book_value
            projected = book_value
        else:
            mus_noncertainty_count += 1
            projected = mus_interval * tainting
        mus_point_projection += projected
        mus_projection_details.append(
            {
                "asset_id_sintetico": asset_id,
                "valor_contabil_liquido_R$_mil": str(book_value),
                "unidades_monetarias_selecionadas": int(
                    record["unidades_monetarias_selecionadas"]
                ),
                "ordens_selecao_mus": "|".join(
                    str(x) for x in record["ordens_selecao_mus"]
                ),
                "intervalo_sistematico_R$_mil": str(mus_interval),
                "item_de_certeza": "Sim" if certainty else "Não",
                "distorcao_assumida_R$_mil": str(book_value),
                "tainting_assumido": str(tainting),
                "projecao_pontual_R$_mil": str(projected),
                "premissa": "Baixa integral assumida somente no cenário sintético; sem contraprestação hipotética",
            }
        )
    notfound = [x for x in exceptions_rows if x["codigo_teste"] == "NAO_LOCALIZADO_SIMULADO"]
    notfound_exposure = sum((Decimal(x["exposicao_potencial_R$_mil"]) for x in notfound), Decimal(0))

    # Avaliação MUS didática: limite superior unilateral de 95% (risco-alvo 5%).
    # Fatores de confiabilidade acumulados: 3,00 para zero erros; 4,75 para um;
    # 6,30 para dois. A ordenação é por tainting decrescente. Para erros abaixo
    # do intervalo, o incremento cumulativo inclui a projeção pontual (fator 1)
    # mais o ajuste de risco; separar ambos evita rotular projeção como risco.
    mus_confidence_factors_95 = [
        Decimal("3.00"), Decimal("4.75"), Decimal("6.30"), Decimal("7.76"),
        Decimal("9.16"), Decimal("10.52"), Decimal("11.84"), Decimal("13.15"),
        Decimal("14.44"), Decimal("15.71"), Decimal("16.96"),
    ]
    projected_taintings = sorted(
        (Decimal(row["tainting_assumido"]) for row in mus_projection_details
         if row["item_de_certeza"] != "Sim"),
        reverse=True,
    )
    if len(projected_taintings) >= len(mus_confidence_factors_95):
        raise ValueError("Ampliar a tabela de fatores MUS para a quantidade de erros projetados")
    mus_basic_precision = mus_confidence_factors_95[0] * mus_interval
    mus_incremental_allowances = []
    for rank, tainting in enumerate(projected_taintings, start=1):
        factor_increment_total = mus_confidence_factors_95[rank] - mus_confidence_factors_95[rank - 1]
        factor_risk_allowance = factor_increment_total - Decimal("1.00")
        projected_error = mus_interval * tainting
        risk_allowance = factor_risk_allowance * projected_error
        mus_incremental_allowances.append({
            "ordem": rank,
            "tainting": tainting,
            "fator_incremental_total": factor_increment_total,
            "fator_allowance_risco": factor_risk_allowance,
            "projecao_pontual": projected_error,
            "allowance_risco": risk_allowance,
            "contribuicao_ajustada_uel": projected_error + risk_allowance,
        })
    mus_projected_noncertainty = sum(
        (item["projecao_pontual"] for item in mus_incremental_allowances), Decimal(0)
    )
    mus_incremental_risk_total = sum(
        (item["allowance_risco"] for item in mus_incremental_allowances), Decimal(0)
    )
    mus_adjusted_noncertainty_total = mus_projected_noncertainty + mus_incremental_risk_total
    mus_upper_error_limit = (
        mus_certainty_error + mus_basic_precision
        + mus_projected_noncertainty + mus_incremental_risk_total
    )
    mus_exceeds_tolerable = mus_upper_error_limit > MATERIALIDADE_EXECUCAO_R_MIL
    mus_exceeds_global = mus_upper_error_limit > MATERIALIDADE_GLOBAL_R_MIL
    mus_risk_conclusion = (
        "Não atende ao critério de aceitação didático: limite superior de erro acima da distorção tolerável; "
        "investigar as exceções, considerar correção e ampliar/redesenhar procedimentos."
        if mus_exceeds_tolerable else
        "Atende ao limite numérico didático; conclusão ainda depende da validade da população e das evidências."
    )

    # Planejamento de tamanho para proporção/atributo: aproximação didática, não amostra monetária.
    z, p, e = 1.96, 0.5, 0.05
    n0 = z*z*p*(1-p)/(e*e)
    n_finite = math.ceil(n0/(1+(n0-1)/N_POP))
    result = {
        "matricula": "202062044",
        "base": base_path.name,
        "lista_verdade": truth_path.name,
        "registros_de_dados": population_count,
        "ids_unicos": len(seen),
        "amostra_aleatoria_simples": {"n": len(random_sample), "seed": args.seed, "reposicao": False, "criterio": "z=1,96; p=0,50; precisão absoluta=5%; correção populacional finita; amostra descritiva, não dimensionamento normativo de auditoria", "objetivo_do_atributo": "presença de ID, classe e três campos monetários na base sintética", "campos_chave_ausentes_na_amostra": aas_rows_with_missing, "limite": "Não é teste de controle da companhia, nem amostra de auditoria sobre registros reais; não sustenta opinião"},
        "amostra_monetaria_MUS": {"n_unidades_monetarias": mus_n, "itens_unicos_selecionados": len(mus_output), "seed_inicio_aleatorio": args.seed + 1, "populacao_valor_liquido_R$_mil": str(sum_nbv), "materialidade_execucao_usada_como_distorcao_toleravel_R$_mil": str(MATERIALIDADE_EXECUCAO_R_MIL), "fator_confianca": str(MUS_CONFIANCE_FACTOR), "risco_amostral_didatico": "5%", "erro_esperado_assumido_R$_mil": "0", "intervalo_sistematico_R$_mil": str(mus_interval), "inicio_aleatorio_R$_mil": str(mus_start), "baixas_ficticias_na_selecao": mus_disposals, "projecao_pontual_ficticia_baixas_R$_mil": str(mus_point_projection), "itens_de_certeza_exposicao_R$_mil": str(mus_certainty_error), "itens_nao_certeza_projetados": mus_noncertainty_count, "baixas_ficticias_selecionadas_detalhe": mus_projection_details, "arquivo_detalhe_projecao": "pt530_detalhe_projecao_mus.csv", "limite": "Estimativa pontual simplificada de erro plantado com tainting de 100%; não é limite superior/confiança estatística e não é estimativa da MDIA3. Fator 3,0 e PM como proxy não são prescrição normativa"},
        "avaliacao_risco_MUS": {
            "nivel_confianca_unilateral": "95%",
            "risco_alvo_de_aceitacao_incorreta": "5% (parâmetro do desenho didático, não risco residual medido)",
            "fatores_acumulados_usados": ["3,00", "4,75", "6,30"],
            "itens_de_certeza_com_erro_assumido": mus_disposals - mus_noncertainty_count,
            "erro_observado_nos_itens_de_certeza_R$_mil": str(mus_certainty_error),
            "erros_projetados_abaixo_do_intervalo": mus_noncertainty_count,
            "precisao_basica_R$_mil": str(mus_basic_precision),
            "allowances_incrementais": [
                {"ordem": item["ordem"], "tainting": str(item["tainting"]),
                 "fator_incremental_total": str(item["fator_incremental_total"]),
                 "fator_allowance_risco": str(item["fator_allowance_risco"]),
                 "projecao_pontual_R$_mil": str(item["projecao_pontual"]),
                 "allowance_risco_R$_mil": str(item["allowance_risco"]),
                 "contribuicao_ajustada_uel_R$_mil": str(item["contribuicao_ajustada_uel"])}
                for item in mus_incremental_allowances
            ],
            "projecao_pontual_erros_nao_certeza_R$_mil": str(mus_projected_noncertainty),
            "allowance_incremental_risco_total_R$_mil": str(mus_incremental_risk_total),
            "contribuicao_ajustada_erros_nao_certeza_R$_mil": str(mus_adjusted_noncertainty_total),
            "projecao_pontual_total_R$_mil": str(mus_point_projection),
            "limite_superior_erro_95_R$_mil": str(mus_upper_error_limit),
            "distorcao_toleravel_R$_mil": str(MATERIALIDADE_EXECUCAO_R_MIL),
            "excede_distorcao_toleravel": mus_exceeds_tolerable,
            "materialidade_global_R$_mil": str(MATERIALIDADE_GLOBAL_R_MIL),
            "excede_materialidade_global": mus_exceeds_global,
            "conclusao": mus_risk_conclusion,
            "metodo": "UEL = erro observado nos itens de certeza + precisão básica + projeção pontual dos erros não certeza + ajuste incremental de risco. Para cada erro: projeção = tainting × intervalo; ajuste de risco = projeção × (diferença entre fatores de confiabilidade consecutivos − 1).",
            "limite": "Aproximação didática com fatores de confiabilidade a 95%; depende de população válida e de erros de superavaliação corretamente identificados. Não é prescrição da NBC TA 530 nem conclusão sobre a MDIA3."
        },
        "amostra_combinada_n": len(combined),
        "selecao_focada": "Censo das regras sintéticas de exceção mais 25 maiores saldos; seleção não estatística e não projetável",
        "consolidado_gerado_R$_mil": {"custo": str(sum_cost), "depreciacao": str(sum_dep), "saldo_liquido": str(sum_nbv)},
        "diferencas_custo_menos_depreciacao_vs_saldo": mismatch_count,
        "itens_com_depreciacao_maior_que_custo": dep_exceeds_cost_count,
        "excecoes_por_regra": {code: len(ids) for code, ids in detected.items()},
        "exposicao_potencial_baixas_nao_registradas_R$_mil": str(disp_exposure),
        "projecao_pontual_MUS_baixas_sinteticas_R$_mil": str(mus_point_projection),
        "projecao_MUS_metodo_limite": "Itens com múltiplas unidades monetárias tratados como certeza; demais exceções selecionadas projetadas por intervalo × tainting. Estimativa didática não é limite superior nem evidência da companhia.",
        "exposicao_potencial_nao_localizados_sinteticos_R$_mil": str(notfound_exposure),
        "materialidade_global_R$_mil": str(MATERIALIDADE_GLOBAL_R_MIL),
        "materialidade_execucao_R$_mil": str(MATERIALIDADE_EXECUCAO_R_MIL),
        "limiar_trivial_R$_mil": str(LIMIAR_TRIVIAL_R_MIL),
        "exposicao_baixas_maior_materialidade_global": disp_exposure > MATERIALIDADE_GLOBAL_R_MIL,
        "comparacao_excecoes_inseridas_identificadas": comparison,
        "limitacao": "Resultados pertencem exclusivamente a um cenário sintético. Sinais, exposições e exceções não são evidência sobre a companhia."
    }
    mus_csv_details = []
    mus_decimal_fields = {
        "valor_contabil_liquido_R$_mil",
        "intervalo_sistematico_R$_mil",
        "distorcao_assumida_R$_mil",
        "tainting_assumido",
        "projecao_pontual_R$_mil",
    }
    for detail in mus_projection_details:
        row = detail.copy()
        for field in mus_decimal_fields:
            row[field] = Decimal(row[field])
        mus_csv_details.append(row)
    write_csv(
        out / "pt530_detalhe_projecao_mus.csv",
        [
            "asset_id_sintetico",
            "valor_contabil_liquido_R$_mil",
            "unidades_monetarias_selecionadas",
            "ordens_selecao_mus",
            "intervalo_sistematico_R$_mil",
            "item_de_certeza",
            "distorcao_assumida_R$_mil",
            "tainting_assumido",
            "projecao_pontual_R$_mil",
            "premissa",
        ],
        mus_csv_details,
    )
    incremental_risk_rows = [
        {
            "indicador": f"Ajuste incremental de risco — erro {item['ordem']}",
            "valor": item["allowance_risco"],
            "unidade": "BRL mil",
            "interpretacao": (
                f"Projeção pontual × ({item['fator_incremental_total']} − 1,00); "
                "separado da projeção pontual do erro."
            ),
        }
        for item in mus_incremental_allowances
    ]
    risk_rows = [
        {"indicador": "Saldo populacional conciliado", "valor": sum_nbv, "unidade": "BRL mil", "interpretacao": "Base sintética; total confirmado por conciliação."},
        {"indicador": "Unidades monetárias selecionadas", "valor": mus_n, "unidade": "unidades", "interpretacao": "Desenho didático com risco-alvo de aceitação incorreta de 5%."},
        {"indicador": "IDs distintos selecionados", "valor": len(mus_output), "unidade": "IDs", "interpretacao": "IDs podem receber mais de uma unidade monetária."},
        {"indicador": "Intervalo sistemático", "valor": mus_interval, "unidade": "BRL mil", "interpretacao": "Saldo líquido da população dividido pelas unidades monetárias."},
        {"indicador": "Baixas fictícias selecionadas", "valor": mus_disposals, "unidade": "itens de 5 plantados", "interpretacao": "Cobertura observada somente neste cenário sintético."},
        {"indicador": "Erro assumido em itens de certeza", "valor": mus_certainty_error, "unidade": "BRL mil", "interpretacao": "Três itens de certeza; erro integral assumido no cenário."},
        {"indicador": "Projeção pontual total", "valor": mus_point_projection, "unidade": "BRL mil", "interpretacao": "Erro dos itens de certeza mais projeção pontual dos demais; não é UEL."},
        {"indicador": "Precisão básica", "valor": mus_basic_precision, "unidade": "BRL mil", "interpretacao": "Fator acumulado 3,00 × intervalo; confiança unilateral aproximada de 95%."},
        {"indicador": "Projeção pontual dos erros não certeza", "valor": mus_projected_noncertainty, "unidade": "BRL mil", "interpretacao": "Soma de tainting × intervalo para os dois erros abaixo do intervalo; componente da projeção pontual e também do UEL."},
        *incremental_risk_rows,
        {"indicador": "Ajustes incrementais de risco — total", "valor": mus_incremental_risk_total, "unidade": "BRL mil", "interpretacao": "Soma do componente de risco, separado da projeção pontual dos erros."},
        {"indicador": "Contribuição ajustada de erros não certeza ao UEL", "valor": mus_adjusted_noncertainty_total, "unidade": "BRL mil", "interpretacao": "Projeção pontual dos erros não certeza + ajustes incrementais de risco; não somar novamente em outra linha."},
        {"indicador": "Limite superior de erro (UEL, 95%)", "valor": mus_upper_error_limit, "unidade": "BRL mil", "interpretacao": "Erro observado em itens de certeza + precisão básica + projeções pontuais não certeza + ajustes incrementais de risco."},
        {"indicador": "Distorção tolerável (proxy) usada", "valor": MATERIALIDADE_EXECUCAO_R_MIL, "unidade": "BRL mil", "interpretacao": "Materialidade de execução usada apenas como proxy didática."},
        {"indicador": "Excesso do UEL sobre distorção tolerável", "valor": mus_upper_error_limit - MATERIALIDADE_EXECUCAO_R_MIL, "unidade": "BRL mil", "interpretacao": mus_risk_conclusion},
        {"indicador": "Razão UEL / distorção tolerável", "valor": mus_upper_error_limit / MATERIALIDADE_EXECUCAO_R_MIL, "unidade": "vezes", "interpretacao": "Acima de 1, o resultado da amostra não sustenta aceitação no limite didático."},
        {"indicador": "Materialidade global acadêmica", "valor": MATERIALIDADE_GLOBAL_R_MIL, "unidade": "BRL mil", "interpretacao": "Benchmark acadêmico de 5% do resultado antes de IR/CSLL."},
        {"indicador": "Excesso do UEL sobre materialidade global", "valor": mus_upper_error_limit - MATERIALIDADE_GLOBAL_R_MIL, "unidade": "BRL mil", "interpretacao": "UEL menos materialidade global acadêmica; comparação auxiliar do cenário."},
    ]
    write_csv(
        out / "pt530_avaliacao_risco_mus.csv",
        ["indicador", "valor", "unidade", "interpretacao"],
        risk_rows,
    )
    (out / "resumo_resultados_testes.json").write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")

    summary_rows = [
        {"teste": "PT530-01 Contagem e unicidade", "populacao": population_count, "excecoes": population_count-len(seen), "exposicao_potencial_R$_mil": "0", "resultado": "500.000 IDs sintéticos únicos"},
        {"teste": "PT500-01 Conciliação de custo bruto", "populacao": population_count, "excecoes": "0", "exposicao_potencial_R$_mil": sum_cost-Decimal("7205695.000"), "resultado": "Total sintético comparado ao custo bruto divulgado; sem evidência real"},
        {"teste": "PT500-02 Depreciação acumulada", "populacao": population_count, "excecoes": str(dep_exceeds_cost_count), "exposicao_potencial_R$_mil": sum_dep-Decimal("3634705.000"), "resultado": "Total sintético comparado ao saldo divulgado; sem evidência real"},
        {"teste": "PT500-03 Recalcular valor líquido", "populacao": population_count, "excecoes": str(mismatch_count), "exposicao_potencial_R$_mil": "0", "resultado": "Custo menos depreciação recalculado em cada linha"},
        {"teste": "PT530-02 AAS descritiva de campos-chave", "populacao": N_POP, "excecoes": aas_rows_with_missing, "exposicao_potencial_R$_mil": "Não aplicável", "resultado": f"n={len(random_sample)} sem reposição; campos-chave ausentes na amostra={aas_rows_with_missing}; teste apenas de qualidade dos dados sintéticos"},
        {"teste": "PT530-03 MUS: seleção e projeção pontual sintética", "populacao": N_POP, "excecoes": f"{mus_disposals} baixas fictícias selecionadas", "exposicao_potencial_R$_mil": mus_point_projection, "resultado": f"n={mus_n} unidades; {len(mus_output)} IDs; intervalo {mus_interval:.3f} BRL mil; projeção pontual {mus_point_projection:.3f} BRL mil; sem inferência para MDIA3"},
        {"teste": "PT530-04 MUS: avaliação do risco de amostragem", "populacao": N_POP, "excecoes": f"UEL 95% = {mus_upper_error_limit:.3f} BRL mil", "exposicao_potencial_R$_mil": mus_upper_error_limit, "resultado": f"UEL excede a distorção tolerável proxy de {MATERIALIDADE_EXECUCAO_R_MIL:.3f} BRL mil; seleção sintética não passa critério de aceitação didático; requer investigação/ampliação no cenário"},
        {"teste": "PT330/530-03 Baixas ainda registradas", "populacao": population_count, "excecoes": len(disp), "exposicao_potencial_R$_mil": disp_exposure, "resultado": "Exceção deliberadamente plantada; comparar com materialidade apenas no cenário"},
        {"teste": "PT330/530-04 Projetos disponíveis ainda em andamento", "populacao": population_count, "excecoes": len(detected.get("CIP_DISPONIVEL_NAO_TRANSFERIDO", [])), "exposicao_potencial_R$_mil": "Não quantificada", "resultado": "Exceção deliberadamente plantada; validar data e depreciação"},
        {"teste": "PT330/530-05 Itens não localizados em vistoria simulada", "populacao": population_count, "excecoes": len(notfound), "exposicao_potencial_R$_mil": notfound_exposure, "resultado": "Atributo de cenário; não é inspeção real"},
        {"teste": "PT265/330-06 Etiquetas ausentes", "populacao": population_count, "excecoes": len(detected.get("ETIQUETA_AUSENTE", [])), "exposicao_potencial_R$_mil": "Não quantificada", "resultado": "Deficiência de rastreabilidade plantada; não constitui distorção quantificada"},
    ]
    write_csv(out / "resultados_procedimentos.csv", ["teste", "populacao", "excecoes", "exposicao_potencial_R$_mil", "resultado"], summary_rows)
    print(json.dumps({"registros": population_count, "amostra_aleatoria": len(random_sample), "amostra_combinada": len(combined), "amostra_mus_itens_unicos": len(mus_output), "amostra_mus_unidades": mus_n, "totais_R$_mil": result["consolidado_gerado_R$_mil"], "exposicao_baixas_R$_mil": str(disp_exposure), "resultados": str(out / "resumo_resultados_testes.json")}, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()
