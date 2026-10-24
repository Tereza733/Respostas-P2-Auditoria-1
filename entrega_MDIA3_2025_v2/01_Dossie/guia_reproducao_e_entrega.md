# Guia passo a passo de reprodução e entrega

**Matrícula:** 202062044. **Versão do pacote:** 2.2, 23/10/2026.

Este guia serve para reproduzir a população e os testes sintéticos e para publicar o material solicitado pelo professor. O pacote não contém dados contábeis individualizados reais da companhia.

## 1. Baixar e extrair o pacote

1. Baixe o ZIP final e extraia-o em uma pasta de sua escolha, por exemplo `Documentos/MDIA3_AUD1_2025`.
2. Abra a pasta extraída. Na raiz, deve estar o `README.md` e as pastas `01_Dossie` a `05_Fontes_e_normas`.
3. Não abra `base_imobilizado_sintetica_500000.csv.gz` por duplo clique: é a população completa comprimida.

**Por quê:** manter código, dados, dicionário, planilha e papéis juntos evita reproduções inconsistentes.

## 2. Conferir o conteúdo acadêmico

1. Leia primeiro `01_Dossie/papeis_trabalho_auditoria.pdf`.
2. Confira a planilha `03_Planilhas/planilha_auditoria_MDI.xlsx` e a matriz `05_Fontes_e_normas/matriz_cobertura_normas.csv`.
3. Abra `02_Base_e_amostras/dicionario_base.pdf` antes de interpretar qualquer campo da população.
4. Verifique que a matrícula aparece como `202062044` e que não há nome pessoal.
5. Mantenha em toda cópia a expressão “sintético” e os avisos de escopo.

**Por quê:** reconciliar totais agregados não converte linhas inventadas em cadastro real nem em evidência de auditoria.

## 3. Instalar Python e dependências

Instale Python 3.10 ou posterior se ainda não estiver disponível. Em Windows, abra PowerShell; em macOS/Linux, abra Terminal. A partir da raiz do repositório, execute:

```bash
python --version
python -m venv .venv
```

Ative o ambiente virtual:

```powershell
# Windows PowerShell
.venv\Scripts\Activate.ps1
```

```bash
# macOS/Linux
source .venv/bin/activate
```

Instale as dependências:

```bash
python -m pip install -r 04_Codigo/requirements.txt
```

Se o sistema não reconhecer `python`, use `python3` nos comandos seguintes.

## 4. Abrir o terminal na pasta correta

Os comandos abaixo precisam ser executados na **raiz** do repositório, o diretório que contém `README.md`.

- **Windows:** no Explorador de Arquivos, abra a pasta extraída, clique na barra de endereço, digite `powershell` e pressione Enter. Confirme a pasta atual com `Get-Location`.
- **macOS/Linux:** no Terminal, use `cd` com o caminho da pasta, por exemplo `cd ~/Documents/MDIA3_AUD1_2025`; confirme com `pwd`.

Não cole os comandos dentro da janela interativa do Python que mostra `>>>`.

## 5. Gerar a população de 500.000 registros

Na raiz, execute no Windows PowerShell:

```powershell
python 04_Codigo\gerar_base_imobilizado.py `
  --output-dir 02_Base_e_amostras `
  --seed 20261021
```

No macOS/Linux:

```bash
python 04_Codigo/gerar_base_imobilizado.py \
  --output-dir 02_Base_e_amostras \
  --seed 20261021
```

A saída substitui a população sintética e seus parâmetros na pasta `02_Base_e_amostras`. O resumo deve indicar 500.000 itens e saldos agregados de custo bruto BRL 7.205.695 mil, depreciação acumulada BRL 3.634.705 mil e valor líquido BRL 3.570.990 mil.

**Por quê:** a semente fixa reproduz as regras de geração. Valores e atributos por item são artificiais; somente os saldos por classe são calibrados à Nota 11.

## 6. Reexecutar as amostras e procedimentos

Execute no Windows PowerShell:

```powershell
$base = '02_Base_e_amostras\base_imobilizado_sintetica_500000.csv.gz'
$truth = '02_Base_e_amostras\registro_excecoes_inseridas.csv'
python 04_Codigo\executar_testes_auditoria.py `
  --base $base --truth $truth `
  --out-dir 02_Base_e_amostras --seed 5302025
```

No macOS/Linux, use:

```bash
base=02_Base_e_amostras/base_imobilizado_sintetica_500000.csv.gz
truth=02_Base_e_amostras/registro_excecoes_inseridas.csv
python 04_Codigo/executar_testes_auditoria.py \
  --base "$base" --truth "$truth" \
  --out-dir 02_Base_e_amostras --seed 5302025
```

As saídas incluem: AAS descritiva de 384 linhas; amostra combinada de 441 IDs; MUS de 606 unidades em 603 IDs; conciliação por classe; flags plantadas e identificadas; comparação das flags; resultados por teste; resumo JSON; e `pt530_detalhe_projecao_mus.csv`, com as cinco baixas sintéticas selecionadas, pontos monetários, classificação de certeza, tainting e projeção individual. No cenário fixado, os 37 itens plantados são reconhecidos pelas regras conhecidas do mesmo gerador. Isso é uma verificação interna do código, não teste independente de auditoria.

A AAS verifica presença de campos-chave na base sintética; não é teste de controle da companhia. A projeção MUS é uma estimativa pontual didática, não limite superior/confiança estatística nem projeção para a MDIA3.

## 7. Regenerar as planilhas editáveis

A partir da raiz:

```bash
python 04_Codigo/criar_planilha.py
python 04_Codigo/criar_amostra_excel.py
```

Os arquivos gerados ficam em `03_Planilhas`. Abra-os no Excel ou LibreOffice Calc. Se uma fórmula não aparecer recalculada, use o comando de recálculo do programa de planilhas; não digite por cima das células de fórmula.

## 8. Abrir CSV no Excel em português

Para uma amostra CSV, ao importar selecione **UTF-8**, separador **ponto e vírgula (`;`)** e decimal **vírgula**. Para a base completa, descompacte o `.gz` com 7-Zip ou use Dados → De Texto/CSV, escolha a mesma codificação e delimitador. A base comprimida é mais prática para armazenar e reproduzir por Python.

**Por quê:** configurações regionais diferentes podem juntar colunas ou exibir acentos/números incorretamente. Os CSVs de saída usam BOM UTF-8, `;` e vírgula decimal.

## 9. Revisão acadêmica final

Antes da submissão, confira no dossiê: benchmark primário e sensibilidade de materialidade; fórmula do analítico de clientes; desenho e limites da amostragem; status de procedimento planejado versus executado; vigência aplicável ao período 2025; e ausência de opinião independente emitida. Confirme com o professor eventuais convenções específicas de formatação ou conteúdo. O percentual de execução de 50%, o fator MUS 3,0 e o limite trivial são premissas didáticas, não regras mandatórias.

## 10. Publicar no GitHub — ação manual

1. Crie o repositório indicado pela disciplina e mantenha o `README.md` na raiz.
2. Carregue a estrutura organizada do pacote, sem renomear a população ou remover os avisos “sintético”.
3. Evite republicar o ZIP original de fontes, a menos que a disciplina autorize sua redistribuição. O README e a relação de fontes registram nomes e links.
4. Abra o repositório por janela anônima (público) ou confira a permissão do professor (privado). Teste o dossiê PDF, XLSX, scripts, matriz e base comprimida.
5. Copie o link do repositório e envie-o no campo indicado pela disciplina até **25/10/2026**, conforme `papeis.docx`.

