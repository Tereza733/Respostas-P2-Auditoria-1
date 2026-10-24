# MDIA3 — auditoria acadêmica simulada, exercício 2025

**Matrícula:** 202062044. **Versão do pacote:** 2.2 — 23/10/2026.

Este repositório reúne um trabalho acadêmico sobre as demonstrações consolidadas de M. Dias Branco S.A. relativas ao exercício encerrado em 31/12/2025. O material não constitui auditoria profissional e não emite opinião independente. A opinião publicada em 26/02/2026 pertence à KPMG.

## Estrutura

```text
01_Dossie/                 Dossiê, modelo acadêmico, comunicações e recomendações
02_Base_e_amostras/        População sintética, dicionário, amostras e resultados
03_Planilhas/              Planilha de auditoria e visualização da amostra
04_Codigo/                 Geradores, testes e dependências
05_Fontes_e_normas/        Fontes, localizadores e matriz NBC/CPC
.gitignore                 Arquivos locais/temporários ignorados pelo Git
```

O dossiê principal está em `01_Dossie/papeis_trabalho_auditoria.pdf` e sua fonte editável está no arquivo `.md` correspondente. A planilha principal é `03_Planilhas/planilha_auditoria_MDI.xlsx`.

## População sintética

`02_Base_e_amostras/base_imobilizado_sintetica_500000.csv.gz` contém 500.000 registros de dados, cada um com ID sintético único, mais o cabeçalho. Os registros não representam bens da companhia. Somente os saldos agregados por classe foram calibrados aos valores da Nota 11. Os valores, datas, unidades, subtipos, etiquetas e flags por item são simulados; a base não comprova existência, titularidade, condição ou avaliação de ativos reais.

## Reprodução

Execute os comandos a partir da raiz do repositório, no diretório que contém este README:

```bash
python -m venv .venv
```

Ative o ambiente virtual no Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

No macOS/Linux:

```bash
source .venv/bin/activate
```

Com o ambiente ativo, instale as dependências:

```bash
python -m pip install -r 04_Codigo/requirements.txt
```

No Windows PowerShell, gere a base e os testes com:

```powershell
python 04_Codigo\gerar_base_imobilizado.py `
  --output-dir 02_Base_e_amostras --seed 20261021
python 04_Codigo\executar_testes_auditoria.py `
  --base 02_Base_e_amostras\base_imobilizado_sintetica_500000.csv.gz `
  --truth 02_Base_e_amostras\registro_excecoes_inseridas.csv `
  --out-dir 02_Base_e_amostras --seed 5302025
python 04_Codigo\criar_planilha.py
python 04_Codigo\criar_amostra_excel.py
```

No macOS/Linux, use:

```bash
python 04_Codigo/gerar_base_imobilizado.py \
  --output-dir 02_Base_e_amostras --seed 20261021
python 04_Codigo/executar_testes_auditoria.py \
  --base 02_Base_e_amostras/base_imobilizado_sintetica_500000.csv.gz \
  --truth 02_Base_e_amostras/registro_excecoes_inseridas.csv \
  --out-dir 02_Base_e_amostras --seed 5302025
python 04_Codigo/criar_planilha.py
python 04_Codigo/criar_amostra_excel.py
```

Se o comando `python` não estiver disponível, use `python3`. Os scripts registram amostras, reconciliações, testes e planilhas. A população gerada contém 500.000 IDs únicos e reconcilia por construção os agregados de custo bruto de BRL 7.205.695 mil, depreciação acumulada de BRL 3.634.705 mil e valor líquido de BRL 3.570.990 mil. Nenhum desses resultados permite inferir achados sobre a MDIA3.

## Critérios de interpretação

A conta do imobilizado foi priorizada por magnitude individual — BRL 3.570.990 mil, 28,43% do ativo — e por seus riscos inerentes, sem ser chamada de “mais material” por definição normativa. A materialidade global de BRL 35.413,500 mil parte de premissa acadêmica de 5% do resultado antes dos tributos e é acompanhada por sensibilidades; os percentuais utilizados não são regras universais.

A amostra aleatória de 384 registros avalia campos-chave da base sintética. A seleção MUS contém 606 unidades monetárias em 603 IDs únicos. A memória `02_Base_e_amostras/pt530_detalhe_projecao_mus.csv` apresenta os cinco itens de baixa sintética selecionados, pontos monetários, itens de certeza, tainting e parcela projetada; o resultado total de BRL 41.785,446 mil é uma estimativa pontual didática, não limite superior nem estimativa sobre registros da companhia. As 37 flags são exceções construídas para verificar regras conhecidas do código, não achados reais nem validação independente da capacidade de detectar erros desconhecidos.

As referências e localizadores das demonstrações e normas estão em `05_Fontes_e_normas/fontes_e_localizadores.md` e na matriz correspondente. Os documentos de origem não são duplicados nesta pasta; os itens e links consultados estão identificados no inventário de fontes.

## Apoio de inteligência artificial

Inteligência artificial foi utilizada como apoio à elaboração deste trabalho acadêmico, com revisão e validação integradas ao processo de produção.
