# Dossiê de papéis de trabalho — MDIA3, exercício encerrado em 31/12/2025

**Matrícula:** 202062044  
**Classificação:** trabalho acadêmico didático; não constitui auditoria profissional nem opinião independente.  
**Entidade em análise:** M. Dias Branco S.A. Indústria e Comércio de Alimentos e controladas.  
**Unidade:** BRL mil, salvo indicação em contrário.  
**Data das demonstrações:** 31/12/2025; comparativo 31/12/2024.  
**Versão do arquivo:** 2.2 — revisão metodológica e de rastreabilidade em 23/10/2026.  
**Data do relatório publicado:** 26/02/2026.  
**Fontes-base:** demonstrações financeiras anuais completas, DFP e demais documentos catalogados em `fontes_e_localizadores.md`; compêndio de NBC TA adotado como referência; pronunciamentos CPC consultados no portal oficial.

**Escopo e vigência normativa:** a matriz cobre individualmente as NBC TAs previstas no guia da disciplina (200 a 600) e registra a versão e vigência do compêndio normativo adotado como referência, consideradas para o exercício encerrado em 31/12/2025. O índice oficial do CFC foi consultado em 22/10/2026. Revisões publicadas em 2026 com vigência para períodos iniciados a partir de 01/01/2027 não foram aplicadas retroativamente. CPCs pertinentes estão mapeados por tema e referenciados no portal oficial. NBC TAs 610, 620, 700, 701, 705, 706, 710 e 720 são referências suplementares ou condicionais, não alegações de cobertura profissional.

> **Aviso de escopo:** valores da companhia foram extraídos de divulgações públicas. A população v2 de 500.000 linhas é integralmente sintética; só os agregados por classe foram calibrados à Nota 11. Os testes computacionais ocorreram sobre essa população artificial, não sobre registros da MDIA3. Nenhuma flag é achado da companhia. A opinião publicada é da KPMG, não deste trabalho.

## 1. Índice e organização

| Código | Papel | Referência principal |
|---|---|---|
| EC | Objeto, critérios e asseguração | NBC TA Estrutura Conceitual; CPC 00 (R2) |
| PT200–PT265 | Ética, termos, qualidade, documentação, fraude, leis, governança, controles | NBC TA 200–265 conforme matriz de cobertura |
| PT300–PT402 | Planejamento, riscos, materialidade, respostas, serviços | NBC TA 300, 315, 320, 330, 402 |
| PT450–PT540 | Distorções, evidência, itens selecionados, confirmação, saldos iniciais, análise, amostragem e estimativas | NBC TA 450, 500, 501, 505, 510, 520, 530, 540 |
| PT550–PT600 | Partes relacionadas, eventos, continuidade, representações e grupos | NBC TA 550, 560, 570, 580, 600 |
| R700 | Modelo de relatório e decisão de opinião (referência suplementar, fora do escopo principal 200–600) | NBC TA 700, 701, 705, 706 |
| BASE | População, dicionário, código, seleção e resultados | CPC 27/NBC TG 27; NBC TA 330, 450, 500, 530 |

Cruzamentos: materialidade e análises estão em `planilha_auditoria_MDI.xlsx`; população, parâmetros, dicionário, flags, amostras e resultados estão em `02_Base_e_amostras/`; códigos em `04_Codigo/`; fontes e matriz normativa em `05_Fontes_e_normas/`. O mapa integral fica no README.

## 2. PT EC — objeto, critérios e tipo de trabalho

O material acadêmico analisa demonstrações financeiras históricas públicas e uma população sintética. Para as demonstrações, o critério é a estrutura de relatório financeiro indicada pela companhia e as NBC TG/CPC aplicáveis. Para os dados artificiais, os critérios são regras de geração expostas no código e no dicionário. O relatório de auditoria publicado é contexto documental, não evidência produzida nesta atividade acadêmica.

Uma auditoria independente requer responsabilidades aceitas, precondições, independência e evidência apropriada e suficiente para segurança razoável. Não houve contratação, acesso à escrituração, confirmações, comunicação com administração/governança ou execução de testes em registros da entidade. A atividade, portanto, é uma análise acadêmica sem asseguração. Não se afirma segurança razoável, asseguração limitada ou opinião profissional própria.

## 3. PT200, PT210, PT220 e PT230 — ética, termos, qualidade e documentação

**PT200:** manter ceticismo diante de estimativas, reconhecimento de receita, possível burla de controles e informações fornecidas pela administração. Este exercício não representa uma auditoria independente contratada e não inclui acesso à escrituração nem evidências privadas. A conclusão fica limitada à análise documental e à simulação.

**PT210:** a contratação real não ocorreu. A minuta acadêmica em `minutas_comunicacoes.pdf` descreve objetivo, alcance, responsabilidades, acesso à informação, estrutura esperada e precondições. Não deve ser assinada nem enviada.

**PT220:** gestão de qualidade para uma auditoria real incluiria competência da equipe, direção, supervisão, revisão, consulta, independência e salvaguardas. Nesta atividade foi usada revisão lógica do conjunto de arquivos e código; não houve revisão independente de auditor habilitado. Risco de qualidade remanescente: atribuição de saldos agregados a itens sintéticos sem razão auxiliar, ausência de evidência externa e necessidade de revisão acadêmica final.

**PT230:** arquivos usam códigos EC/PT/R/BASE/EXT; o índice e a matriz de cobertura vinculam normas e procedimentos. Arquivos devem permanecer versionados; as duas sementes fixas são 20261021 (geração) e 5302025 (AAS). Em auditoria real, a montagem e o encerramento do arquivo seguiriam a NBC TA 230 e política aplicável. Esta pasta é versão acadêmica; preservar scripts e sumários juntos.

## 4. PT240, PT250, PT260 e PT265 — fraude, legislação e comunicações

**Fraude (PT240):** risco presumido de reconhecimento de receita fora do período é elevado por natureza. O próprio relatório da KPMG identifica reconhecimento de receitas como principal assunto de auditoria e descreve testes em entregas de dezembro, recálculo do corte e análise de devoluções de janeiro. Isso é evidência do procedimento publicado pela KPMG, não teste repetido neste trabalho. Outros riscos a planejar: lançamentos manuais, estimativas enviesadas e burla de controles pela administração. Respostas reais incluiriam indagação, teste de lançamentos de fechamento, testes de estimativas retrospectivas e corte de vendas/baixas. Não executados sobre dados internos.

**Leis e regulamentos (PT250):** notas revelam provisões cíveis, trabalhistas e tributárias, subvenções estaduais e requisitos contratuais/ambientais em financiamento. Planejar leitura de atos legais, conciliação de cálculos, carta de assessores jurídicos e indagação de não conformidade. O dossiê público não fornece processo individual ou evidência de cumprimento; portanto, não conclui conformidade.

**Governança (PT260):** em trabalho real, comunicar estratégia, cronograma, riscos significativos, independência, limitações, distorções e deficiências aos responsáveis pela governança. As DFs informam que a companhia contratou a KPMG para auditoria e revisão, declara que não foram prestados serviços conflitantes e relata outros serviços de asseguração limitada do relatório integrado por BRL 120 mil (aproximadamente 16,7% dos honorários de auditoria); a política divulgada submete serviços à análise prévia do Comitê de Auditoria. São informações públicas atribuídas à administração, não avaliação independente da independência da KPMG. O inventário de fontes também relaciona o Estatuto Social. A análise de governança nesta versão limita-se às divulgações das demonstrações financeiras e não conclui sobre a composição ou as atribuições formais dos órgãos. Não houve comunicação externa; a minuta em `minutas_comunicacoes.pdf` não foi enviada.

**Controles (PT265):** nenhuma deficiência da companhia foi constatada. A tabela abaixo reporta somente hipóteses da simulação ou recomendações para o desenho do exercício.

| Condição simulada | Critério esperado | Causa hipotética | Efeito possível | Recomendação didática | Status |
|---|---|---|---|---|---|
| 5 ativos baixados ainda aparecem no cadastro artificial; BRL 39.000 mil líquidos | Atualização tempestiva do subledger e conciliação com razão | Hipótese criada pelo gerador | Possível superavaliação/erro de baixa; excede materialidade global ilustrativa | Vincular baixa a autorização, documento de alienação/abate, bloqueio do ativo e conciliação periódica | Exceção intencional; não é achado real |
| 12 itens sem etiqueta artificial | Identificação rastreável e inventário físico | Hipótese plantada | Risco de rastreabilidade; efeito monetário não quantificado | Política de etiqueta, reconciliação física/cadastro e investigação de divergências | Exceção intencional; não é achado real |
| 12 projetos com data sintética de disponibilidade, ainda em andamento | Transferir para classe em uso e iniciar depreciação quando disponível | Falha de comunicação projeto-contabilidade, hipotética | Classificação e depreciação inadequadas | Termo de comissionamento e revisão mensal de projetos concluídos | Exceção intencional; não é achado real |
| 8 itens “não localizados” em vistoria fictícia | Inspeções documentadas com resolução e aprovação | Resultado fabricado | Risco de existência, sem prova sobre a entidade | Contagem física rotativa e apuração formal | Não houve inspeção real |

## 5. PT300 e PT315 — estratégia global, materialidade e riscos

**Estratégia:** foco nos riscos de reconhecimento/corte de receita, mensuração de intangível e imobilizado, estoque e custos, recebíveis/perda esperada, contingências e instrumentos financeiros. As DFs informam que o Projeto Simplifique, com migração para SAP S/4HANA e integração de 47 sistemas legados, foi concluído em 2024; em 2025, o foco foi capturar ganhos da nova base (PDF, p. 9) [1]. Isso eleva a atenção de auditoria a acessos, mudanças, interfaces, conversão de dados, relatórios e lançamentos manuais, sem evidenciar por si só uma deficiência. Período: exercício findo em 31/12/2025. A evidência aqui limita-se às demonstrações, notas e relatório publicado; não houve teste de TI.

**Informações-base:** ativo total 12.559.343; imobilizado 3.570.990; intangível 2.416.590; clientes 1.843.604; estoques 1.675.464; caixa 1.888.270; passivo circulante 2.235.103; receita líquida 10.437.548; resultado antes de IR/CSLL 708.270. Variações 2025 vs 2024: ativo total -1,6%; imobilizado -0,5%; receita líquida +8,0%; resultado antes de IR/CSLL -14,0%. Fonte: balanço e notas das DFs completas 2025 e DFP [1] [3].

**Materialidade (PT320):** a NBC TA 320 não escolhe uma conta “mais material” nem impõe um benchmark ou percentual único. Para esta simulação, o resultado antes de IR/CSLL foi escolhido provisoriamente por ser uma medida de desempenho potencialmente relevante em uma entidade lucrativa; o cálculo usa 5% do resultado consolidado reportado (BRL 708.270 mil) [1]. O julgamento é frágil à volatilidade: o resultado caiu 14,0% em 2025 e a linha de subvenções estaduais para investimentos é expressiva. Por isso, a análise compara também exclusão mecânica dessa linha, receita e ativo total; nenhum benchmark alternativo é assumido automaticamente como “correto”. A materialidade para execução de 50% e o limite trivial de 5% da global também são premissas acadêmicas, sujeitas a revisão pelo auditor responsável, não percentuais normativos.

| Nível | Fórmula | Valor BRL mil | Natureza |
|---|---|---:|---|
| Global | 708.270 × 5% | 35.413,500 | Premissa didática; não é limite normativo |
| Execução | 35.413,500 × 50% | 17.706,750 | Julgamento conservador para o cenário, não percentual obrigatório |
| Trivial | 35.413,500 × 5% | 1.770,675 | Limite didático; “claramente trivial” depende também da natureza |

**Sensibilidade relevante:** a DRE apresenta BRL 463.419 mil na linha de subvenções estaduais para investimentos [1], valor equivalente a cerca de 65,4% do resultado antes de tributos. Sem concluir que essa receita seja não recorrente, a exclusão mecânica apenas dessa linha para sensibilidade deixaria BRL 244.851 mil e produziria materialidade global de BRL 12.242,550 mil, execução de BRL 6.121,275 mil e trivial de BRL 612,128 mil. Como alternativas de benchmark, 0,5% da receita líquida de BRL 10.437.548 mil resulta em global de BRL 52.187,740 mil, execução de BRL 26.093,870 mil e trivial de BRL 2.609,387 mil; 1% do ativo total de BRL 12.559.343 mil resulta em global de BRL 125.593,430 mil, execução de BRL 62.796,715 mil e trivial de BRL 6.279,672 mil, aplicando-se as mesmas proporções didáticas de 50%/5%. A distância entre cenários mostra que a seleção do benchmark requer julgamento e conhecimento dos usuários, estabilidade e qualidade do resultado. O valor primário de BRL 35.413,500 mil foi mantido para tornar explícito o efeito do benchmark reportado; não se declara que seja a única escolha adequada. Materialidades específicas por classe/transação/divulgação não foram quantificadas.

**Escolha da conta para a base obrigatória:** imobilizado é a maior linha individual entre as principais rubricas de ativo e combina magnitude com riscos inerentes. Isso justifica a prioridade didática, mas não afirma que a NBC TA 320 defina uma “conta de maior materialidade”.

| Rubrica publicada | Saldo 2025 (BRL mil) | Participação do ativo total | Fator de risco predominante |
|---|---:|---:|---|
| Imobilizado | 3.570.990 | 28,43% | Existência, direitos, baixas, mensuração, classificação e projetos em andamento |
| Intangível | 2.416.590 | 19,24% | Goodwill/marcas e premissas de impairment |
| Caixa e equivalentes | 1.888.270 | 15,03% | Existência, direitos, restrições e confirmação |
| Clientes | 1.843.604 | 14,68% | Existência, direitos, aging e perda esperada |
| Estoques | 1.675.464 | 13,34% | Existência física, custo e valor realizável líquido |

Assim, **imobilizado foi selecionado para a base** por magnitude individual e risco, não por ser automaticamente “a conta mais material”. A seleção não substitui materialidade no nível das demonstrações nem avaliação por afirmação. Goodwill/intangível pode ter risco de estimativa qualitativamente superior; receita permanece área de risco de fraude.

**Riscos por afirmação (PT315):**

| Conta/área | Risco inerente e afirmações | Prioridade/resposta planejada |
|---|---|---|
| Receita líquida 10.437.548 | Reconhecimento/cut-off; ocorrência, exatidão, corte, apresentação; presunção de risco de fraude no reconhecimento | Alto: documentos de entrega/aceite, teste de dezembro e janeiro, devoluções, contratos, lançamentos e reconciliação faturamento-razao |
| Intangível 2.416.590 | Goodwill 1.243.915 e marcas 790.410 sem amortização; valoração/impairment e divulgações, risco de estimativa elevado | Alto: revisar CGUs, orçamento, fluxos, taxa de desconto 13,04%, crescimento terminal 3,9%, análise de sensibilidade e viés retrospectivo |
| Imobilizado 3.570.990 | Existência, direitos, integridade, classificação, depreciação, baixa, corte e impairment; inclui ROU sob Nota 13 | Alto por saldo (28,4% do ativo) e complexidade: cadastro, títulos, adições/baixas, inspeção, recálculo, projetos em andamento e vinculação ao razão |
| Clientes 1.843.604; ECL 60.051 | Existência/direitos e valoração; aging e expectativa de crédito | Alto/moderado: confirmações, recebimentos posteriores, aging, dados/modelo e revisão de saldos >360 dias |
| Estoques 1.675.464; perda 31.481 | Existência, integridade, custo médio, corte e valor realizável líquido | Alto: inventário físico em data adequada, custo, obsolescência, preço de venda subsequente |
| Contingências | Provisões 200.718; possíveis divulgadas 2.307.733 | Alto qualitativo: carta jurídica, completude de processos, probabilidade, mensuração e divulgação; possíveis não são passivo reconhecido |
| Caixa/derivativos | Caixa 1.888.270; derivativos ativos 80.579 e passivos 30.046 | Existência, direitos, valor justo, classificação e risco de contraparte; confirmações diretas e recálculo |
| Empréstimos e arrendamentos | Financiamentos e empréstimos 1.419.965; passivo de arrendamento 322.005 | Integridade, mensuração, classificação corrente e covenant; confirmações, contratos, recálculo e busca de passivos |

**Classificação de risco significativo:** o risco de fraude no reconhecimento de receita é presumido pela NBC TA 240 e tratado como significativo no planejamento, sujeito à resposta documentada da NBC TA 330. As demais áreas acima são prioridades de risco inerente. Sem razão, controles, dados granulares e avaliação completa dos fatores da NBC TA 315, não se atribui formalmente “significativo” a cada risco nem se infere deficiência de controle. A designação “alto” na tabela é prioridade acadêmica, não conclusão de auditoria.

## 6. PT330 — respostas e programas de auditoria

Todos os procedimentos desta tabela são **planejados para uma auditoria real**; a execução indicada é somente o processamento das regras artificiais no arquivo da base.

| Risco | Procedimento previsto | Execução possível no pacote | Evidência faltante/limite |
|---|---|---|---|
| Imobilizado: custo e saldo líquido | Reconciliar por classe, recalcular valor líquido, testar altas/baixas e direitos | Conciliação e identidade por linha executadas na população sintética; 500.000 IDs únicos | Sem acesso ao razão, cadastro patrimonial, notas fiscais, títulos, contratos e documentos de baixa neste exercício |
| Existência física | Selecionar do cadastro para inspeção e da inspeção para cadastro | Oito sinais de não localizado foram plantados; não houve vistoria | Nenhuma evidência física real |
| Corte e transferência de projetos | Inspecionar aceite/comissionamento; verificar início de depreciação | Doze datas de disponibilidade fictícias identificadas | Documentos de engenharia e data de uso real ausentes |
| Receita/cut-off | Amostrar notas/entregas de dezembro e devoluções de janeiro | Apenas análise da nota, dos saldos e do PAA publicado | Sem acesso a base transacional de vendas, documentos de entrega/aceite, faturas e razão |
| Intangível/impairment | Testar dados e modelo, taxa de desconto, crescimento, CGUs e sensibilidades | Revisão documental das premissas publicadas | Sem acesso ao modelo integral de avaliação, projeções, contratos de aquisição e dados internos de mercado |
| Estoques | Acompanhar contagem física, custo e valor realizável líquido | Comparação de saldo e nota | Sem observação de contagem física nem acesso ao razão, fichas de custo ou vendas subsequentes |
| Clientes | Confirmar saldos e testar perda esperada | Análise de aging publicado | Sem acesso a razão auxiliar, confirmações, histórico de recebimentos ou modelo de perda esperada |
| Contingências | Carta de assessores jurídicos e avaliação legal | Análise de divulgações | Sem cartas jurídicas, autos ou pareceres no escopo documental examinado |
| Caixa e dívida | Confirmações, extratos e contratos/covenants | Análise de saldos e cláusulas divulgadas | Sem confirmação bancária, contratos completos ou extratos no escopo deste exercício |

## 7. PT402 — prestadores de serviços

As fontes documentais catalogadas não apresentam uma lista completa de prestadores que processam informação financeira, descrição de sistemas terceirizados ou relatórios tipo 1/tipo 2. O RAI não foi tratado como evidência de eficácia de controles. Não se conclui que prestadores relevantes não existam. Em auditoria real, solicitar mapa de terceiros, serviços, processos e controles relevantes; obter relatórios aplicáveis, avaliar controles complementares do usuário e testar controles ou executar procedimentos alternativos. Nesta atividade, status: não avaliado por falta de informação.

## 8. PT450 — mapa de distorções

O único valor monetário conhecido no cenário é a baixa artificialmente não registrada em cinco itens. Os registros somam custo bruto de BRL 48.500 mil, depreciação acumulada de BRL 9.500 mil e valor líquido de BRL 39.000 mil. Se, apenas para o cenário, os bens tivessem sido alienados sem qualquer produto ou compensação, sua baixa reduziria o imobilizado e o resultado antes de tributos em BRL 39.000 mil; o efeito tributário e no patrimônio líquido não foi estimado. Se houve produto de alienação, o resultado correto dependeria da contraprestação. Portanto, BRL 39.000 mil é exposição potencial do cenário, não distorção identificada na MDIA3.

| Item simulado | Classificação no cenário | Efeito se não corrigido | Correção hipotética | Corrigida pela administração? |
|---|---|---|---|---|
| 5 baixas ainda registradas | Factual quanto à condição inserida; mensuração final depende de evidência de alienação | Imobilizado potencialmente superavaliado em BRL 39.000 mil; 1,10× global, 2,20× execução e 5,51% do resultado antes de tributos | Sob a hipótese restrita de nenhuma contraprestação: retirar custo de BRL 48.500 mil e depreciação de BRL 9.500 mil; reconhecer perda líquida de BRL 39.000 mil | Não aplicável: não existe administração real no cenário |
| 8 itens marcados “não localizados” | Sinal sintético de existência; não é resultado de inspeção | Exposição agregada de 3,848 em BRL mil (equivalente a BRL 3.848 em moeda corrente), abaixo do limite trivial; relevância qualitativa somente se confirmada por evidência real | Investigar existência e eventual baixa; não lançar ajuste apenas com a flag artificial | Não aplicável |
| 12 projetos disponíveis ainda em andamento | Inconsistência factual sintética; efeito contábil requer julgamento | Classificação e depreciação potencialmente incorretas; valor não quantificado | Confirmar comissionamento, custo, vida útil e residual; recalcular depreciação se aplicável | Não aplicável |
| 12 etiquetas ausentes | Deficiência de rastreabilidade simulada, não distorção monetária por si só | Efeito contábil não quantificado | Corrigir identificação e rastreabilidade após verificação real | Não aplicável |

A avaliação cumulativa limita-se ao valor de BRL 39.000 mil no cenário e supera os limites global e de execução adotados. Os demais itens não são somados a esse valor: alguns são qualitativos, não quantificados ou dependem de confirmação, e podem se sobrepor. Não há valor corrigido ou não corrigido pela administração da companhia, porque nenhuma distorção real foi testada ou comunicada. A amostra aleatória não foi usada para projetar as flags plantadas.

## 9. PT500, PT501 e PT505 — evidência, itens selecionados e confirmações

A evidência obtida neste trabalho consiste em divulgações públicas da entidade e dados inventados pelo script. Divulgações são adequadas para entender o saldo declarado, não para provar existência, titularidade, completude ou mensuração de itens individuais. O arquivo sintético concilia aritmeticamente com a Nota 11, mas isso demonstra somente a regra de geração.

**PT501:** estoques, contingências e segmento foram analisados documentalmente. O grupo reporta um segmento de negócios; não há dados granulares de segmento independente para teste. Para estoque, foram identificadas classes, custo médio e perda publicada, mas sem observação física. Para litígios, há provisões e perdas possíveis divulgadas, sem acesso a autos/cartas jurídicas. Não se afirma teste de auditoria real.

**PT505:** não foram enviadas confirmações. Em trabalho real, definir amostra de saldos de bancos, clientes, fornecedores, advogados e contrapartes de derivativos, controlar endereçamento/resposta sob controle do auditor, investigar exceções e aplicar alternativas para não respostas. O pacote inclui minuta e um formulário vazio de controle didático por categoria, sem contatos, saldos, população, amostra real ou registro de envio. Não foi criada planilha de respostas reais. Carta de confirmação não substitui documentação de resposta e autenticidade.

## 10. PT510 — saldos iniciais

Tratar como exercício de auditoria inicial didática: comparar saldos de abertura de 2024/2025 e políticas publicadas, conferir consistência de apresentação, saldos comparativos e eventual modificação do auditor anterior. O relatório publicado de 2025 contém opinião não modificada da KPMG; isso não comprova saldos iniciais por este trabalho. Sem papéis do auditor anterior, DFs anteriores auditadas, auxiliares e evidência de abertura, a NBC TA 510 não pode ser concluída. Solicitar comunicação ao antecessor conforme autorização e avaliar procedimentos alternativos.

## 11. PT520 — procedimentos analíticos

Os cálculos abaixo usam valores consolidados publicados, em BRL mil. Variação = (2025 / 2024) − 1. Dias de clientes = saldo final comparável / receita líquida × 365; é uma proxy simplificada, não prazo contratual nem média diária. O limiar de BRL 17.706,750 mil é gatilho de investigação baseado na PM didática, não critério automático de erro.

| Indicador | Cálculo/base | 2025 | 2024 | Resultado/investigação |
|---|---|---:|---:|---|
| Clientes — expectativa proporcional | saldo total de clientes 2024 × (receita 2025 / receita 2024) | 1.843.604 | 1.803.940,402 esperados | Diferença de BRL 39.663,598, cerca de 2,24× PM; investigar composição corrente/não corrente, aging, prazo, mix, moeda, concentração, recebimentos posteriores e ECL de BRL 60.051 |
| Receita líquida | 10.437.548 / 9.662.833 − 1 | 10.437.548 | 9.662.833 | +8,0%; decompor por mês, produto, preço/volume, corte e descontos |
| Resultado antes de IR/CSLL | 708.270 / 823.185 − 1 | 708.270 | 823.185 | −14,0%; investigar margem, financeiro, subvenções e itens não recorrentes sem presumir natureza |
| Ativo total | 12.559.343 / 12.768.867 − 1 | 12.559.343 | 12.768.867 | −1,6% |
| Imobilizado líquido | 3.570.990 / 3.590.675 − 1 | 3.570.990 | 3.590.675 | −0,5%; conciliar adições, depreciação, baixas, transferências e impairment |
| Dias de clientes — proxy | saldo total de clientes / receita líquida × 365 | 64,47 | 63,08 | +1,39 dia; razão de saldos finais, não aging nem prazo médio validado |
| Caixa gerado operacional | DFC consolidada | 1.407.929 | 591.669 | Aumento expressivo; investigar capital de giro, juros e derivativos |
| Liquidez corrente | ativo circulante / passivo circulante | 2,61x | 2,20x | Melhora; não substitui análise de vencimentos e fluxos |
| Liquidez sem estoques | (ativo circulante − estoques) / passivo circulante | 1,86x | 1,58x | Indicador simplificado |
| Caixa / passivo circulante | caixa e equivalentes / passivo circulante | 0,84x | 0,79x | Não considera restrições ou vencimentos intraperíodo |

A expectativa de clientes usa o saldo comparável total de 2024 de BRL 1.670.045 mil (incluindo BRL 1.667.866 mil circulante e BRL 2.179 mil não circulante). Aplicando crescimento da receita de BRL 9.662.833 mil para BRL 10.437.548 mil, a expectativa simples é BRL 1.803.940,402 mil. O saldo de 2025 excede essa expectativa em BRL 39.663,598 mil. A diferença supera o limiar de investigação, mas **não é distorção identificada**; pode refletir mix, prazo, moeda, concentração ou outros fatores. A análise não substitui dados mensais, orçamento, aging, razão auxiliar ou recebimentos.

## 12. PT530 — população e amostragem

A população v2 contém 500.000 IDs sintéticos únicos, sem repetição de linhas para atingir volume. A unidade amostral é um item fictício por ID; o arquivo comprimido UTF-8 com BOM usa `;` e vírgula decimal; ao descompactar, contém 500.001 linhas com cabeçalho. Os saldos individuais são rateios artificiais e não correspondem a um cadastro real. A reconciliação agregada com a Nota 11 foi executada por classe e por identidade aritmética.

**Seleção aleatória descritiva (n=384):** semente 5302025, sem reposição. A regra de cálculo ilustra proporção conservadora de 50%, z=1,96, precisão absoluta de 5% e correção para população finita. O atributo definido foi presença de ID, classe e três valores monetários. Na amostra, 0/384 registros tinham campos-chave ausentes. Trata-se de verificação de qualidade da base sintética, não de teste de controle da companhia nem de dimensionamento completo de amostra de auditoria segundo a NBC TA 530; não se projeta para a MDIA3.

**Seleção combinada:** 441 IDs únicos, formada pela união da seleção aleatória de 384, dos 25 maiores saldos e do censo de exceções sintéticas, após deduplicação. Os itens direcionados e o censo de flags não são projetáveis.

**MUS sistemática didática:** a população é o saldo líquido sintético de BRL 3.570.990 mil. O tamanho ilustrativo é `ceil(3,0 × 3.570.990 / 17.706,750) = 606` unidades monetárias; a materialidade para execução foi usada apenas como proxy provisória de distorção tolerável. O intervalo é BRL 5.892,722772 mil, o início aleatório reproduzível é BRL 3.875,512203 mil e foram selecionados 603 IDs distintos. As 606 unidades e a regra sistemática estão em `amostra_monetaria_MUS.csv`; a semente do início é 5302026. PM, fator 3,0, erro esperado zero e fórmula não são prescrições da NBC TA 530.

**Memória da projeção no cenário:** o CSV `pt530_detalhe_projecao_mus.csv` e o JSON de resultados mostram, para cada baixa plantada selecionada, o saldo, os pontos monetários, o tratamento como item de certeza, tainting assumido e parcela projetada. Sob a hipótese estritamente didática de baixa integral sem contraprestação, três itens de certeza somam BRL 30.000 mil; dois itens abaixo do intervalo, com tainting de 100%, projetam BRL 5.892,722772 mil cada. A soma reproduzível é BRL 41.785,445545 mil, enquanto o censo das cinco baixas no mesmo cenário soma BRL 39.000 mil. A diferença é o efeito da projeção por intervalo dos dois itens não classificados como certeza; não é uma distorção adicional conhecida nem prova de erro de cálculo.

| ID sintético | Saldo líquido (BRL mil) | Pontos MUS | Unidades monetárias | Certeza | Tainting assumido | Parcela projetada (BRL mil) |
|---|---:|---|---:|---|---:|---:|
| SIM-IMOB-003001 | 12.000 | 203, 204 | 2 | Sim | 100% | 12.000 |
| SIM-IMOB-003002 | 10.000 | 205, 206 | 2 | Sim | 100% | 10.000 |
| SIM-IMOB-003003 | 8.000 | 207 | 1 | Sim | 100% | 8.000 |
| SIM-IMOB-003004 | 5.000 | 208 | 1 | Não | 100% | 5.892,722772 |
| SIM-IMOB-003005 | 4.000 | 209 | 1 | Não | 100% | 5.892,722772 |
| **Total** | **39.000** | — | **7** | — | — | **41.785,445545** |

Os pontos 203–209 são os números de seleção monetária no intervalo sistemático; duas unidades de amostragem recaem em cada um dos dois primeiros IDs. Os valores e IDs são artificiais e identificam somente a simulação.

Essa estimativa pontual simplificada não é limite superior nem intervalo de confiança: não foram calculados fatores incrementais de confiança ou uma probabilidade de exceder distorção tolerável. A NBC TA 530, itens 14–15, requer projetar distorções quando pertinente e avaliar se os resultados dão base razoável para conclusões; ela não prescreve um único limite superior numérico para todo método. Como a amostra é aplicada a uma população artificial e o erro foi plantado, o resultado não sustenta conclusão sobre a companhia. Uma auditoria real exigiria evidência válida, investigação da causa e efeito, avaliação da distorção projetada e do risco de amostragem, além de redesenho do plano conforme a população e a distorção tolerável.

A contagem/unicidade, reconciliação, identidade por linha e regras foram examinadas sobre 100% da base sintética. O confronto 37/37 entre flags plantadas e identificadas é autoteste do gerador/código com sua lista-verdade, não taxa de detecção, validação independente ou evidência de auditoria.

## 13. PT540 — estimativas contábeis

Estimativa mais sensível: recuperabilidade de goodwill e marcas, saldo conjunto de BRL 2.034.325 mil (goodwill BRL 1.243.915 mil; marcas BRL 790.410 mil), sem amortização e sujeitos a teste de impairment. A administração informou modelo de fluxo de caixa descontado, cinco anos mais perpetuidade, crescimento médio anual das receitas de 6,5%, taxa de desconto de 13,04% e crescimento terminal de 3,9%; impairment não reconhecido. Isso apresenta incerteza e sensibilidade relevantes, dado julgamento de projeções, margens e taxa.

A taxa de desconto subiu de 11,64% em 2024 para 13,04% em 2025, aumento de 140 pontos-base; o crescimento terminal divulgado permaneceu em 3,9%. Como ilustração relativa, o fator de perpetuidade é (1+g)/(r−g):

| Cenário ceteris paribus | Taxa r | Crescimento g | Fator (1+g)/(r−g) | Variação vs. base |
|---|---:|---:|---:|---:|
| Base 2025 | 13,04% | 3,9% | 11,37 | — |
| Taxa 2024 | 11,64% | 3,9% | 13,42 | +18,1% |
| Taxa +100 pb | 14,04% | 3,9% | 10,25 | −9,9% |
| Taxa −100 pb | 12,04% | 3,9% | 12,76 | +12,3% |
| Crescimento −50 pb | 13,04% | 3,4% | 10,73 | −5,6% |
| Crescimento +50 pb | 13,04% | 4,4% | 12,08 | +6,3% |

Essa comparação mede apenas sensibilidade do fator de perpetuidade, mantendo todo o restante constante; não é valor justo nem cálculo do valor recuperável. Sem fluxos projetados por UGC, headroom e modelo da administração, não é possível quantificar perda por impairment. Procedimentos reais incluiriam avaliar método/UGCs, orçamento, previsões, dados, taxa de desconto, crescimento, viés retrospectivo e divulgações.

## 14. PT550 — partes relacionadas

A Nota 14 identifica controlador, controladas, joint operations e empresas relacionadas a administradores/acionista; avaliar completude, identificação e divulgação também à luz do CPC 05 (R1). Há vendas/serviços, fretes, obras, locações, saldos a receber e a pagar. Saldos consolidados relevantes divulgados incluem fornecedores a pagar para partes relacionadas de BRL 6.353 mil, outros créditos/adiantamentos e pagamentos; transações consolidadas de vendas aparecem agregadas. Procedimentos reais: cruzar cadastro de fornecedores/clientes com administradores e acionistas, inspecionar atas, contratos, termos e preços, conciliar saldos, identificar transações não divulgadas e avaliar condições. Sem atas, cadastro interno e razão, completude não foi testada.

## 15. PT560 — eventos subsequentes e corte da pesquisa

Data final do exame documental: 26/02/2026, data de aprovação/relatório indicada nas DFs. A avaliação de reconhecimento e divulgação de eventos subsequentes considera também CPC 24. A página pública de RI lista a divulgação das DFs anuais de 2025 em 26/02/2026 e apresentação de resultados em 27/02/2026; a janela a considerar vai de 31/12/2025 até a data de autorização/relatório. Não foi identificada nas DFs completas fornecidas uma nota separada intitulada “eventos subsequentes”. A página pública de Documentos CVM foi consultada, mas sua extração dinâmica não permitiu verificar exaustivamente todas as categorias e comunicações de janeiro a 26/02/2026. Portanto, não se conclui que não houve eventos relevantes; esta lacuna deve ser resolvida em trabalho real por pesquisa integral, leitura de atas e indagação à administração.

Procedimento real: ler atas e publicações até a data do relatório, indagar administração, rever resultados/caixa após encerramento, atualizar cartas jurídicas e avaliar eventos que forneçam evidência sobre condições existentes em 31/12 (ajuste) ou condições novas relevantes (divulgação). A página de documentos CVM dinâmica de 2026 foi consultada; itens posteriores a 26/02, incluindo atas de março/abril, ficam fora da data de corte e não são tratados como evidência de condições existentes na data-base sem análise.

## 16. PT570 — continuidade operacional

Indicadores publicados: caixa e equivalentes consolidados de BRL 1.888.270 mil; ativo circulante BRL 5.830.994 mil; passivo circulante BRL 2.235.103 mil; liquidez corrente 2,61x; geração operacional de caixa BRL 1.407.929 mil; empréstimos e financiamentos na Nota 16 de BRL 1.419.965 mil e passivos de arrendamento BRL 322.005 mil. Nota 16 informa que a companhia não incorria em hipóteses de restrição de covenants em 31/12/2025. Esses indicadores não provam ausência de incerteza: faltam previsões de fluxo de caixa, cronograma integral de necessidades, linhas disponíveis, covenants completos e eventos adversos pós-data.

Planejar: testar previsões e premissas, datas de vencimento, covenants, fontes de liquidez, compromissos de capex/dividendos e cenários de estresse; avaliar se há incerteza material e se divulgação é adequada. Com os dados públicos consultados, não se observa por si só indicador que permita concluir sobre continuidade, nem base para afirmar incerteza material. Conclusão: insuficiência de evidência independente para opinião sobre continuidade.

## 17. PT580 — representações formais

Minuta didática em `minutas_comunicacoes.pdf` contempla responsabilidade por demonstrações e controles, completude de informação, partes relacionadas, contingências, eventos subsequentes, estimativas e distorções. Não foi obtida assinatura. Representação formal é evidência necessária em auditoria real, mas não substitui evidência documental, externa ou física. Não utilizar como carta real ou atribuir declaração a administradores da MDIA3.

## 18. PT600 — grupo e componentes

As DFs consolidadas incluem controladas com 100% de participação [1], incluindo Jasmine, Darcel/Cacama e entidades no exterior; algumas entidades estrangeiras estavam inoperantes/em encerramento. A Nota 11 descreve imobilizado consolidado; a companhia informa segmento único reportável. Há operação em conjunto Tergran, reconhecida conforme a participação, e empreendimento em conjunto pelo método de equivalência. As políticas de consolidação são analisadas à luz do CPC 36 (R3); CPC 15 (R1) é pertinente apenas quando houver combinação de negócios/goodwill aplicável.

A atividade não dispõe de balancetes por componente, materialidade de componente, lista jurídica completa, eliminações, conversões cambiais nem instruções/papéis de auditores de componentes. Por isso, o escopo e a significância de componentes não foram avaliados quantitativamente; não se infere que existam ou não auditores componentes, nem que diferenças entre demonstrações individuais e consolidadas provem falha de eliminação. Uma auditoria real definiria o grupo/perímetro, identificaria componentes e seus riscos, estabeleceria materialidade de grupo/componente, dirigiria/revisaria o trabalho e testaria consolidação, políticas e eliminações conforme NBC TA 600 (R2), aplicável a auditorias de grupo iniciadas em/ou após 01/01/2024.

## 19. Conclusão integrada e natureza da opinião

O imobilizado consolidado de BRL 3.570.990 mil (28,43% do ativo) foi escolhido para a população sintética por magnitude individual e riscos inerentes. A seleção não significa que seja automaticamente “a conta de maior materialidade” normativa. O reconhecimento de receita segue como risco presumido de fraude e principal assunto publicado pela KPMG; intangível exige análise de estimativas; clientes, estoques, contingências, derivativos, dívida e caixa também requerem respostas próprias. A mudança SAP/Simplifique aparece apenas como contexto público; controles de TI, migração, interfaces e lançamentos não foram testados.

A materialidade primária ilustrativa é BRL 35.413,500 mil global, BRL 17.706,750 mil para execução e BRL 1.770,675 mil trivial; a sensibilidade excluindo mecanicamente a linha de BRL 463.419 mil de subvenção estadual reduz os níveis e evidencia risco de seleção do benchmark. A diferença analítica de clientes é BRL 39.663,598 mil, acima do limiar adotado, e exige investigação; não é erro identificado. Para impairment, só foi possível analisar a sensibilidade relativa do fator de perpetuidade; não houve acesso ao modelo, fluxos ou headroom por UGC.

| Área/risco — rastreabilidade | Procedimento e suporte | Resultado documentado | Conclusão e limite |
|---|---|---|---|
| Receita e corte (PT240/PT330) | DF analíticos, PAA publicado e programa de entregas/corte | Receita +8,0%; nenhum teste transacional próprio | Risco presumido persiste; PAA e testes publicados são da KPMG |
| Imobilizado (PT500/PT530) | Conciliação por classe; AAS e MUS sobre base sintética | 500.000 IDs; 37 flags; 5 baixas selecionadas; projeção pontual BRL 41.785,446 mil | Simulação apenas; não é achado nem estimativa para a MDIA3 |
| Clientes e perda esperada (PT520/PT540) | Saldo 2024 × crescimento da receita; comparação à PM | Diferença BRL 39.663,598 mil > PM BRL 17.706,750 mil | Investigar aging, recebimentos e modelo; não é erro comprovado |
| Goodwill e marcas (PT540) | Premissas divulgadas e sensibilidade do fator terminal | Sensibilidade feita; valor recuperável não recalculado | Sem fluxos/headroom por UGC, perda não quantificável |
| Estoques (PT501/PT330) | Revisão de saldo, custos e perda divulgados | Sem contagem, teste por item ou venda subsequente | Só divulgações; testes físicos permanecem planejados |
| Caixa, dívida e derivativos (PT505/PT520/PT570) | Indicadores públicos; programa de confirmações/contratos | Saldos/índices analisados; sem confirmação ou inspeção contratual | Não prova existência, direitos ou valor justo |
| Provisões e contingências (PT250/PT501) | Notas e plano de carta jurídica/autos | Sem carta ou análise individual de processo | Completude e mensuração não concluídas |
| Demonstrações consolidadas (PT600) | Perímetro e políticas divulgadas; sem papéis por componente | Controladas identificadas; sem balancetes por componente | Materialidade não quantificada; não implica falha |

A base v2 contém 500.000 itens individualizados sintéticos, com IDs únicos, e reconcilia por construção aos agregados de custo, depreciação e saldo líquido da Nota 11. Foram executados testes computacionais sobre a população sintética, seleção aleatória descritiva e MUS didática. As 37 flags pertencem exclusivamente ao cenário; BRL 39.000 mil é exposição condicional das cinco baixas plantadas. A estimativa pontual MUS de BRL 41.785,446 mil não é limite superior nem projeção para a MDIA3. Não foram feitos procedimentos em registros da companhia, confirmações, inspeção física, testes de TI, análise de dados operacionais ou validação de consolidação.

O roteiro mestre pede julgamento sobre tipo de opinião; o guia específico de papéis e entrega veda afirmar opinião profissional independente. Adota-se a leitura prudente: **não há base probatória para formar ou emitir opinião própria**. Isso não é opinião sem ressalva, com ressalva, adversa ou abstenção sobre as demonstrações da companhia. A opinião publicada pertence à KPMG. O modelo condicional não deve ser apresentado como relatório emitido.

## 20. Uso de inteligência artificial

Inteligência artificial foi utilizada como apoio à elaboração deste trabalho acadêmico, com revisão e validação integradas ao processo de produção.

## Referências documentais e links

O inventário em `fontes_e_localizadores.md` identifica os documentos consultados, complementares e não utilizados nos cálculos. As fontes principais são as demonstrações financeiras anuais completas de 2025, a DFP de 2025, o compêndio de NBC TA adotado como referência, as instruções acadêmicas e os índices oficiais do CFC e do CPC. O uso e as limitações de cada fonte estão descritos no inventário.

### Fontes referenciadas

- [1] Demonstrações Financeiras Anuais Completas 2025 — M. Dias Branco, Relações com Investidores.
- [2] Normas Brasileiras de Contabilidade — Auditoria Independente, Conselho Federal de Contabilidade.
- [3] Demonstrações Financeiras Padronizadas — CVM, Dados Abertos.
- [4] Pronunciamentos emitidos — Comitê de Pronunciamentos Contábeis.

[1]: https://ri.mdiasbranco.com.br/informacoes-financeiras/demonstracoes-financeiras/ "Demonstrações financeiras da M. Dias Branco — RI"
[2]: https://cfc.org.br/tecnica/normas-brasileiras-de-contabilidade/nbc-ta-de-auditoria-independente/ "Normas Brasileiras de Contabilidade — Auditoria Independente, CFC"
[3]: https://dados.cvm.gov.br/dataset/cia_aberta-doc-dfp "DFP — Dados Abertos da CVM"
[4]: https://www.cpc.org.br/CPC/Documentos-Emitidos/Pronunciamentos "Pronunciamentos emitidos pelo CPC"
