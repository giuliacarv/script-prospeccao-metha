# Cobertura da matriz integral

A [matriz de mensagens](Metha-Mensagens-por-Etapa.xlsx) reúne os 14 documentos originais do acervo no snapshot `b507edaf39b596761e8aa58b1892d4afa9b22f5b`.

**14 linhas de matriz, uma por documento; 1.600 registros de origem; e 173 partes de texto integral de apoio.** O total de registros inclui mensagens da Metha, falas de leads em simulações, instruções, tabelas, exemplos e roteiros de reunião. Não representa 1.600 modelos prontos para envio.

## Fontes contempladas

| Arquivo de origem | Formato | Registros |
| --- | --- | ---: |
| [Copydrill/v9_1/copydrill_v9_1.html](Copydrill/v9_1/copydrill_v9_1.html) | HTML | 139 |
| [doug.tensao/v10/Metha Jurídica — Script V10 FINAL.md](doug.tensao/v10/Metha%20Jur%C3%ADdica%20%E2%80%94%20Script%20V10%20FINAL.md) | MD | 46 |
| [doug.tensao/v10/Metha V10 — Stress Test_ 6 Conversas + Plano de Emergência.md](doug.tensao/v10/Metha%20V10%20%E2%80%94%20Stress%20Test_%206%20Conversas%20%2B%20Plano%20de%20Emerg%C3%AAncia.md) | MD | 130 |
| [doug.tensao/v10/script-doug.tensao-v10.2.html](doug.tensao/v10/script-doug.tensao-v10.2.html) | HTML | 133 |
| [doug.tensao/v10/script-doug.tensao-v10.html](doug.tensao/v10/script-doug.tensao-v10.html) | HTML | 136 |
| [Karnage/v9_1/metha_script_v9_3_rotas.html](Karnage/v9_1/metha_script_v9_3_rotas.html) | HTML | 76 |
| [Outros/Playbook Comercial Metha — Karnage.md](Outros/Playbook%20Comercial%20Metha%20%E2%80%94%20Karnage.md) | MD | 39 |
| [Outros/Playbook_Comercial_Metha_V7.0_Final.pdf](Outros/Playbook_Comercial_Metha_V7.0_Final.pdf) | PDF | 172 |
| [Outros/Playbook_Comercial_Metha_V7.2_Janela_de_Ouro.pdf](Outros/Playbook_Comercial_Metha_V7.2_Janela_de_Ouro.pdf) | PDF | 87 |
| [Outros/Playbook_Comercial_Metha_V8.md](Outros/Playbook_Comercial_Metha_V8.md) | MD | 134 |
| [Outros/Playbook_Comercial_Metha_V8.pdf](Outros/Playbook_Comercial_Metha_V8.pdf) | PDF | 172 |
| [Outros/Playbook_Comercial_Metha_V8_IA_WhatsApp.md](Outros/Playbook_Comercial_Metha_V8_IA_WhatsApp.md) | MD | 147 |
| [Outros/Playbook_Comercial_Metha_V8_Salesbot_Kommo_Sem_IA.md](Outros/Playbook_Comercial_Metha_V8_Salesbot_Kommo_Sem_IA.md) | MD | 146 |
| [Pra quem se frustou com agência anterior (Copydrill).md](Pra%20quem%20se%20frustou%20com%20ag%C3%AAncia%20anterior%20%28Copydrill%29.md) | MD | 43 |

## Tipos de conteúdo

| Tipo | Registros |
| --- | ---: |
| Mensagem Metha em simulação | 220 |
| Fala do Lead em simulação | 164 |
| Instrução / contexto da fonte | 70 |
| Mensagem Metha | 917 |
| Mensagem e conduta da fonte | 127 |
| Retomada e instrução da fonte | 12 |
| Instrução / tabela da fonte | 44 |
| Exemplo simulado / não enviar como fato | 16 |
| Roteiro de reunião humana | 16 |
| Exemplo / não enviar automaticamente | 14 |

## Preservação e conferência

- Todos os 1.600 registros possuem referência na matriz e texto completo na aba Mensagens integrais. Os valores foram conferidos após a exportação do XLSX.
- Os sete Markdown completos foram reconstruídos a partir da aba Contexto integral e comparados com as fontes do Git, sem diferenças.
- Todas as páginas dos PDFs estão no contexto integral: 58 do V7.0 Final, 32 do V7.2 Janela de Ouro e 58 do V8.
- Os 146 IDs do catálogo IA foram encontrados no PDF V8. Os hashes declarados para os textos do Markdown conferem. A diferença de texto da mensagem 051 entre essas fontes foi preservada.
- Todos os blocos identificados nos HTMLs foram extraídos: bolhas de conversa, copies de playbook, mensagens de roteiro e textos de emergência. As falas dos leads possuem tipo e coluna próprios.
- O PDF V7.0 Final e o PDF V8 são idênticos byte a byte. Ambos foram mantidos no inventário e na planilha, sem deduplicação que apague a origem.
- As 96 mensagens adaptadas da primeira entrega permanecem na aba Adaptações iniciais e não se misturam com a extração literal.

## Critérios de leitura

Os blocos delimitados de Markdown são preservados com seu conteúdo literal. Nas fontes em prosa que misturam mensagem e orientação, a seção completa foi mantida como Mensagem e conduta da fonte. Isso evita inventar uma separação de bolhas que o documento não estabelece.

A extração dos HTMLs preserva palavras, pontuação e links externos. Ênfases de HTML são representadas por asteriscos e sublinhados de WhatsApp. Horários, botões de navegação e outros elementos de interface foram separados do corpo da mensagem. O texto visível completo continua no contexto integral.

Nos PDFs, o texto foi extraído das caixas originais de mensagem, mantendo as quebras de linha físicas. As caixas de tabelas foram classificadas como instruções. O PDF original continua disponível para conferir o layout.

Cada documento ocupa uma única linha na matriz. As mensagens integrais são reunidas na coluna da etapa atribuída, identificadas por código, tipo e título. Consulte a aba Mensagens integrais para ver localização, contexto e arquivo de cada ocorrência. A matriz não cria versões comerciais novas nem uma sequência obrigatória.

Textos extensos permanecem completos no arquivo, mesmo quando excedem a altura máxima de linha do Excel. Use a barra de fórmulas ou abra a célula para leitura integral.

A classificação por etapa serve à consulta. A planilha não atualiza preços, comprova cases nem valida referências sazonais. Esses elementos foram conservados conforme cada documento de origem.
