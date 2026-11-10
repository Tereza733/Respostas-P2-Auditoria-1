# Dicionário de dados — população sintética de imobilizado

**Matrícula:** 202062044. **Versão da base:** 2.0. **Data contábil de referência:** 31/12/2025. **População:** 500.000 registros de dados; 500.001 linhas no CSV descompactado, incluindo o cabeçalho. **Arquivo:** `base_imobilizado_sintetica_500000.csv.gz`.

> **Aviso:** todos os IDs, linhas, datas, unidades, subtipos, etiquetas, flags e valores por item foram gerados artificialmente. Eles não são cadastro da M. Dias Branco, nem evidência de existência, direitos, integridade, avaliação ou condição dos bens. Apenas os saldos agregados por classe da Nota 11 foram calibrados. O rateio individual de custo e depreciação é sintético e não reconstitui o auxiliar patrimonial, a política de depreciação ou as vidas úteis da companhia. Não use os registros como se fossem dados reais.

## Justificativa da conta e materialidade

O balanço consolidado de 31/12/2025 apresenta imobilizado líquido de **BRL 3.570.990 mil**, equivalente a **28,43%** do ativo total de BRL 12.559.343 mil. A Nota 11 divulga custo bruto de BRL 7.205.695 mil e depreciação acumulada de BRL 3.634.705 mil. Entre as principais rubricas individuais do ativo apresentadas, o imobilizado é a maior por valor. A escolha da população também considera risco de existência, direitos, integridade, baixas, mensuração, classificação, projetos em andamento e impairment.

Isso é uma priorização acadêmica por magnitude e risco — não significa que a NBC TA 320 designe uma conta como “a mais material”. Materialidade é julgada para as demonstrações como um todo e para execução; riscos e afirmações também são avaliados por natureza, complexidade e circunstâncias. A base não separa ativos próprios de direitos de uso, não comprova titularidade/gravames e não representa a quantidade real de bens da entidade.

**Fonte do saldo:** M. Dias Branco S.A., Demonstrações Financeiras Anuais Completas 2025, balanço consolidado e Nota 11, páginas impressas 60–62, exercício findo em 31/12/2025, valores em BRL mil. Consulte `../05_Fontes_e_normas/fontes_e_localizadores.md` para a relação dos arquivos e links oficiais.

## Unidade e reconciliação agregada

Cada registro corresponde a um **item fictício individual**, identificado por ID único. Os 500.000 registros não são linhas copiadas para atingir uma contagem: os custos e atributos artificiais variam, e a unicidade do ID foi testada em 100% da população. A definição de uma unidade de reconhecimento de imobilizado depende de julgamento e política da entidade; o exercício não presume que cada linha corresponda a um bem do cadastro real.

| Classe contábil publicada | Registros sintéticos | Custo bruto (BRL mil) | Depreciação acumulada (BRL mil) | Saldo líquido (BRL mil) |
|---|---:|---:|---:|---:|
| Edificações | 3.000 | 1.740.776 | 548.812 | 1.191.964 |
| Máquinas e equipamentos | 210.000 | 3.682.384 | 2.388.537 | 1.293.847 |
| Móveis e utensílios | 160.000 | 145.342 | 97.227 | 48.115 |
| Veículos | 10.000 | 256.948 | 127.743 | 129.205 |
| Instalações | 40.000 | 572.492 | 306.773 | 265.719 |
| Imobilizações em andamento | 30.000 | 415.229 | 2.220 | 413.009 |
| Outros | 47.000 | 392.524 | 163.393 | 229.131 |
| **Total** | **500.000** | **7.205.695** | **3.634.705** | **3.570.990** |

O gerador distribui os valores agregados da Nota 11 por IDs fictícios e preserva, em reais inteiros, a identidade `valor_contabil_liquido = custo_historico − depreciacao_acumulada`. A alocação de depreciação não usa as datas sintéticas, vida útil, padrão de consumo ou método contábil. O valor de depreciação acumulada de BRL 2.220 mil divulgado para a classe “imobilizações em andamento” é preservado somente no rateio agregado de reconciliação; não se conclui que projetos em andamento específicos deveriam estar depreciando nem que essa classificação esteja correta. A incerteza não é resolvida pelos dados públicos disponíveis.

## Variáveis do CSV

| Campo | Tipo/formato | Significado e limite |
|---|---|---|
| `asset_id_sintetico` | Texto único | ID gerado para rastreabilidade da simulação; não existe no cadastro da entidade. |
| `registro_sintetico` | Texto | Rótulo explícito “SIM — POPULAÇÃO SINTÉTICA”. |
| `classe_contabil` | Categoria | Uma das sete classes agregadas da Nota 11; linhas individuais foram alocadas artificialmente à classe. |
| `subtipo_sintetico` | Categoria | Rótulo fictício de tipo de item; não descreve ativo real. |
| `unidade_ficticia` | Categoria | Unidade fictícia `UNIDADE-SIM-01` a `UNIDADE-SIM-08`, sem correspondência com fábrica real. |
| `data_capitalizacao_sintetica` | Data ISO | Data artificial. Não é documento de aquisição, capitalização, propriedade ou competência e não alimenta cálculo de depreciação. |
| `data_disponivel_uso_sintetica` | Data ISO ou vazia | Em 12 projetos foi inserida a data artificial 01/01/2025 para demonstrar uma exceção qualitativa de classificação. Não comprova comissionamento nem início de uso. |
| `status_operacional_sintetico` | Categoria | Estado inventado; cinco itens de máquinas aparecem como baixados antes do encerramento e mantidos no cadastro sintético; projetos permanecem “Em andamento”. |
| `data_baixa_sintetica` | Data ISO ou vazia | Data artificial de baixa para os cinco casos plantados; não indica alienação real nem recebimento de contraprestação. |
| `etiqueta_fisica_sintetica` | Texto ou vazio | Etiqueta artificial; 12 campos vazios foram plantados. Não houve inspeção física. |
| `resultado_vistoria_sintetica` | Categoria | “Não selecionado” ou oito flags artificiais de “Não localizado no cenário sintético”; não é resultado de vistoria real. |
| `custo_historico_R$_mil` | Decimal em texto | Parcela sintética de custo bruto, em BRL mil, três casas decimais (precisão de BRL 1). |
| `depreciacao_acumulada_R$_mil` | Decimal em texto | Parcela sintética alocada da depreciação acumulada, na mesma unidade. Não é cálculo por item a partir de vida útil ou data. |
| `valor_contabil_liquido_R$_mil` | Decimal em texto | Custo sintético menos depreciação sintética; calculado em cada linha. |

## Premissas e método de geração

`gerar_base_imobilizado.py` usa NumPy e semente padrão 20261021. Para cada classe, o script cria a quantidade de IDs definida no código, distribui o custo total em valores positivos inteiros de BRL e aloca a depreciação de modo limitado pelo custo, fechando exatamente com os totais divulgados. O valor líquido é calculado como diferença. No cenário de cinco baixas, custo bruto de BRL 48.500 mil e depreciação de BRL 9.500 mil geram exposição potencial sintética de BRL 39.000 mil. Em todos os outros registros, as distribuições são uma convenção de geração, não uma descrição do portfólio real.

O método **não** infere taxa, vida útil, método linear, data efetiva de disponibilidade, impairment, componente de direito de uso, propriedade ou valor residual. A versão 2.0 removeu do arquivo os campos de taxa/vida útil e o subtipo “terreno”, pois a base não tem evidência que sustente esses atributos ou sua relação com a depreciação. As datas restantes são marcadores fictícios e não são insumos do rateio. O CPC 27 requer julgamento sobre unidade de reconhecimento e tratamento contábil; este dataset não simula a aplicação completa do pronunciamento a ativos reais.

## Exceções plantadas e comparação com o teste

O gerador cria `registro_excecoes_inseridas.csv` como lista-verdade da própria simulação. O programa de testes compara essa lista com as flags capturadas pelo código. O resultado 37/37 confirma somente que regras conhecidas reconheceram os itens que o mesmo gerador marcou; não mede sensibilidade independente, eficácia de controles, taxa de erro real ou qualidade da auditoria.

| Código de exceção | Inseridos | Exposição de cenário | Tratamento correto |
|---|---:|---:|---|
| `BAIXA_NAO_REGISTRADA` | 5 | BRL 39.000 mil de valor líquido | Exposição condicional ao cenário; resultado final dependeria de prova de alienação, contraprestação, custos de baixa e demais fatos. |
| `CIP_DISPONIVEL_NAO_TRANSFERIDO` | 12 | Não quantificada | Flag artificial de data/status; não calcular depreciação sem evidência de disponibilidade, custo, vida útil, residual e política. |
| `ETIQUETA_AUSENTE` | 12 | Não quantificada | Problema de rastreabilidade simulado, não distorção monetária automática. |
| `NAO_LOCALIZADO_SIMULADO` | 8 | 3,848 em BRL mil (equivalente a BRL 3.848 em moeda corrente) | Rótulo de resultado fictício; nenhuma vistoria ocorreu e não se deve lançar ajuste. |

## Amostragem e procedimentos executados sobre a base

A contagem da população, unicidade, conciliação por classe, identidade por linha, campos-chave e regras de exceção foram reexecutadas em dados sintéticos. O resumo dos parâmetros é `resumo_resultados_testes.json`; as saídas individuais indicadas no README ficam em `../02_Base_e_amostras/`.

1. **Seleção aleatória descritiva:** 384 registros sem reposição, semente 5302025. A aproximação usa z=1,96, proporção conservadora de 50%, precisão de 5% e correção para população finita. O atributo operacionalizado foi presença de ID, classe e três campos monetários; a amostra teve zero campos-chave ausentes. Isso é um teste de qualidade da base sintética, não teste de controle nem amostra com evidência sobre a MDIA3.
2. **Seleção combinada:** 441 IDs únicos após unir a seleção de 384, os 25 maiores saldos e o censo das flags; seleção dirigida não é projetável.
3. **MUS sistemática:** população monetária de BRL 3.570.990 mil; fator didático 3,0; PM de BRL 17.706,75 mil usada apenas como proxy provisória de distorção tolerável; 606 unidades monetárias em 603 IDs únicos; intervalo BRL 5.892,722772 mil; início aleatório reproduzível no script. Os cinco itens de baixa plantada foram selecionados.
4. **Ilustração de projeção:** tratando os erros plantados como tainting de 100%, três itens de certeza somam BRL 30.000 mil; os dois itens selecionados abaixo do intervalo projetam BRL 5.892,722772 mil cada. A estimativa pontual simplificada é BRL 41.785,445545 mil, contra BRL 39.000 mil de exposição conhecida no censo sintético. Não foi calculado limite superior de erro/amostragem; o fator 3,0 não é usado como limite de confiança. Nenhuma dessas quantias é erro projetado da MDIA3.

A seleção probabilística MUS pressupõe população e valores válidos, definição de distorção tolerável e avaliação dos erros encontrados. Aqui todos esses itens são artificiais; a projeção é apenas demonstração aritmética. A aplicação em auditoria real exigiria refazer o desenho, confirmar valor contábil, investigar diferenças e avaliar a incerteza de amostragem conforme NBC TA 530.

## Formato regional e reprodução

A base comprimida é CSV UTF-8 com BOM, delimitador ponto e vírgula e vírgula decimal nos campos monetários. Para Excel/LibreOffice em português, importar usando UTF-8, `;` e vírgula decimal. O `.gz` deve ser descompactado para importação manual; o próprio script lê o arquivo comprimido.

