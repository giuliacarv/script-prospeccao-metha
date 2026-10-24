# Revisão da organização — 24/10/2026

A revisão reorganiza o acervo de scripts, incluindo a importação do Drive da PR 2. O ponto de recuperação anterior é a revisão Git `416d181902d4ad2c963c038dd121c25c7dbfb88f`.

## O que foi corrigido

- Pastas genéricas de importação, famílias soltas na raiz e nomes extensos foram substituídos por uma estrutura por função, cenário e versão.
- Um nome da importação continha `< >`, incompatíveis com Windows. Todos os caminhos de materiais migrados agora têm até 63 caracteres, sem espaços ou acentos; o mapa preserva os nomes anteriores.
- A página inicial agora distingue 105 arquivos de fontes, 45 documentos na matriz e 60 complementos ainda sem extração. A nota de origem vazia é identificada à parte.
- Os links entre os documentos V5, os caminhos dos modelos JSON/CSV e 2.472 referências de arquivo nas células da matriz acompanham a nova estrutura.
- O inventário passa a registrar SHA-256 atual para todas as fontes e derivados catalogados, além do hash do snapshot anterior e da origem. As cópias exatas são identificadas por conteúdo.
- `.gitattributes` impede conversão automática de quebras de linha: o acervo mantém bytes consistentes entre Windows e outros sistemas.
- A manutenção ganhou um gerador determinístico de índices e uma validação local com Python, sem pacotes adicionais.

## Evidências de preservação

| Verificação | Resultado |
| --- | --- |
| Mapa anterior → atual | 117 arquivos, todos com destino preservado |
| Fontes idênticas em bytes | 100 de 105 |
| Outras cinco fontes | Apenas os destinos de links locais do V5 foram atualizados |
| Blocos copiáveis nas fontes Markdown | Hashes preservados, inclusive nos cinco documentos com links atualizados |
| Matriz | Valores e fórmulas das seis abas comparados; somente caminhos completos de arquivo mudaram |
| Estrutura do XLSX | Quatro XMLs de planilha tiveram referências atualizadas; estilos, tabelas e demais partes mantidos |
| Mensagens da matriz | 2.171 IDs M únicos preservados |
| Modelos Kommo | 43 IDs, mensagens e condições preservados; referências de origem atualizadas |

O [registro de integridade](../catalogo/matriz-integridade.json) e o [inventário](inventario.md) permitem repetir as verificações. Hashes históricos dentro da matriz continuam descrevendo o snapshot de extração; os hashes atuais estão no catálogo.

## Divergências de fonte preservadas

| Material | Divergência ou limite |
| --- | --- |
| [Markdown V8](../playbooks/v8/playbook.md) | O título interno começa como V7.0 |
| [PDF V7.0](../playbooks/v7.0/playbook-final.pdf) e [PDF V8](../playbooks/v8/playbook.pdf) | Conteúdo idêntico em bytes; identidades de origem mantidas |
| [Karnage](../abordagens/karnage/v9.1/script-v9.3-rotas.html) | Pasta de origem V9.1, nome V9.3 e título interno V9 aplicado |
| [Doug V10](../abordagens/doug-tensao/v10/) | Inclui HTMLs V10 e V10.2 como variantes |
| [Script de janeiro](pendencias/script-janeiro-20k30d.md) | Nova leitura do Drive confirmou zero bytes |
| [Prospecção ativa — fragmento](../scripts/whatsapp/legado/prospeccao-ativa-fragmento.md) | A fonte contém uma única linha |
| Word/Google Docs da importação anterior | São cópias em texto Markdown, sem garantia de conservar a formatação original |

Duplicidades exatas adicionais de PDFs e áudios aparecem no inventário. Nomes semelhantes, datas de exportação ou versões maiores não foram usados como prova de equivalência, autoria ou aprovação.

## Continuidade

1. Obter uma cópia com conteúdo do script de janeiro ou confirmar que era um marcador.
2. Decidir quais das 60 fontes complementares merecem extração para ampliar a matriz.
3. Fazer a seleção editorial da versão e dos cenários que a equipe usará, verificando a fonte vigente antes do cadastro no CRM.

A revisão organiza documentos e referências. A validação local não mede desempenho comercial, verifica conteúdo falado nas mídias ou comprova implantação no Kommo.
