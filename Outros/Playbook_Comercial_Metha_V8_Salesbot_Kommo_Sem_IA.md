# Metha — Playbook Salesbot Kommo, sem IA

Versão 1.0 | 10/10/2026 | Base: Playbook Comercial Metha V7.0 atualizado.

## 1. O que este arquivo entrega

Especificação para construir chatbot no editor visual do Salesbot. Não é um arquivo importável: o Kommo não executa Markdown como bot. Contém campos, módulos, menus, condições, pausas, passagem humana, cadências e biblioteca literal de mensagens. Nenhum recurso de IA deve ser ativado.

Textos aprovados foram preservados no catálogo. A mensagem 011 incorpora literalmente a última edição do bloco 73103, inclusive “continuam/aumentam”. Novos menus são textos de interface desta adaptação, identificados separadamente. Não substituir a apresentação, os argumentos ou a devolutiva por menus.

O bot executa escolhas explícitas e regras. Giulia interpreta relatos, aprova rota e contexto, constrói a primeira leitura, escolhe oferta e negocia. Não atribuir ao bot capacidade de resumir, diagnosticar ou deduzir intenção.

## 2. Recursos usados e limites

Construir em **Configurações → Ferramentas de comunicação → Salesbots**, ou pelo editor de automações do funil; conferir os rótulos na conta. Usar Mensagem, botões, Outra resposta, Sem resposta, Condição, Validação, Pausa, ações de campos/tarefas e Parar Salesbot. Inserir variáveis pelo seletor do editor; nomes lógicos deste documento não são sintaxe Kommo.

- Usar até três botões por pergunta. Confirmar suporte do conector WhatsApp instalado. Se não suportar, acrescentar instrução de resposta numérica e validar por igualdade exata.
- Sinônimos somente explícitos e testados. Não usar “contém sim”, “contém agência”, “contém não” para classificar mensagens: “não tenho agência” não significa “tenho agência”.
- Outra resposta: encaminhar para Giulia. Áudios, anexos, dúvidas, múltiplas respostas e textos ambíguos também vão para ela.
- Pausa com mensagem recebida e cronômetro permite saídas alternativas; conectar a resposta ao cancelamento da pendência, nunca ao próximo follow-up.
- Adotar um único bot conversacional por lead. A documentação atual descreve situações de interrupção entre bots; não depender de concorrência.
- Não presumir interrupção automática quando Giulia escreve. Antes de assumir, parar a execução ativa e bloquear novas ativações. Testar o comando manual na conta.
- Formulário preenchido, agenda, assinatura e pagamento exigem confirmação manual ou integração determinística. Cliques em links não comprovam conclusão.
- Sem confirmação do plano, do conector e dos passos disponíveis, esta é uma especificação configurável, não instalação validada. Disparos devem usar o tipo de mensagem permitido pelo canal; falha de envio cria tarefa, não avanço fictício.

## 3. Um funil; estados da conversa em campos

| Etapa | Entrada | Saída |
|---|---|---|
| Base a ativar | Prospect validado | Abordagem efetivamente enviada |
| Ativado | Primeiro envio registrado | Resposta recebida ou encerramento |
| Conversa e qualificação | Resposta recebida | Contexto mínimo validado por Giulia |
| Pré-diagnóstico | Coleta/formulário em andamento | Devolutiva real entregue e reunião pertinente |
| Reunião | Convite pertinente após devolutiva | Reunião realizada e decisão sobre proposta |
| Proposta e negociação | Oferta aprovada e enviada | Aceite ou recusa |
| Formalização | Aceite comercial | Contratação confirmada |
| Ganho / Perdido | Critério terminal confirmado | Reativação somente deliberada |

Formulário enviado, explicação de anúncios, CTA ignorado e no-show são campos, não colunas. Silêncio encerra uma cadência; não comprova falta de fit. Giulia escolhe se perde ou mantém retomada futura com tarefa e data.

## 4. Campos mínimos de controle

Criar os campos do processo no lead; nome/telefone/e-mail no contato. Campos técnicos podem ficar em grupo separado.

| Campo lógico | Tipo / opções | Quem preenche |
|---|---|---|
| SB modo | Lista: LIBERADO, BOT, HUMANO, BLOQUEADO | Bot/Giulia |
| SB módulo | Texto: identificador do módulo | Bot |
| SB checkpoint | Texto: último nó concluído | Bot |
| SB pendência | Lista: nenhuma, abertura, foco, contexto, formulário, convite, reunião, proposta, formalização | Bot/Giulia |
| SB retomada | Número: 0, 1, 2, 3 | Bot |
| SB próximo envio | Data/hora, quando disponível; tarefa com vencimento como referência | Operação/integrador |
| Não contatar | Checkbox | Giulia/bot mediante opção inequívoca |
| Rota | Lista: desconhecida, anuncia, parou, nunca anunciou | Menu/Giulia |
| Lado | Lista: reclamante, empresarial, misto, desconhecido | Menu/Giulia |
| Entende anúncios | Lista: desconhecido, sim, precisa explicar | Giulia; menu registra declaração |
| Objetivo e tese | Texto | Giulia a partir de relato |
| Contexto validado | Checkbox | Giulia |
| Resumo aprovado | Texto | Giulia; usado na 010 |
| Histórico de mídia | Texto: verba, plataforma, tese e resultado relatados | Giulia/formulário |
| Atendimento e capacidade | Texto | Giulia/formulário |
| Investimento viável | Lista: desconhecido, compatível, a avaliar, incompatível | Giulia |
| Canal de coleta | Lista: formulário, WhatsApp, dispensado | Escolha/Giulia |
| Formulário status | Lista: não elegível, elegível, sugerido, enviado, recebido, coleta WhatsApp, encerrado | Bot/Giulia/integração |
| Formulário URL / enviado em | URL / data | Operação/bot quando disponível |
| Devolutiva texto | Texto | Giulia |
| Devolutiva aprovada / enviada | Checkboxes | Giulia / operação |
| Reunião status | Lista: não oferecida, convite, interessado, horários, marcada, realizada, no-show, reagendar, encerrada | Bot/Giulia/agenda |
| Reunião data / link | Data / URL | Giulia/agenda |
| Proposta status / URL | Lista: preparar, enviada, negociação, aceita, recusada / URL | Giulia |
| Contratação confirmada | Checkbox | Giulia ou integração validada |
| Motivo de perda | Lista: sem interesse, fora de perfil, orçamento, momento, concorrente, sem retorno, contato inválido, não contatar | Giulia |

Não usar valor da causa como ticket ou prova de liquidez. Não preencher interpretação comercial automaticamente a partir de número isolado. Registro bruto de resposta, se o editor permitir captura, é dado pendente de revisão, não classificação confiável.

## 5. Contrato de execução de todos os módulos

Antes de iniciar: contato principal e canal corretos; não contatar desmarcado; modo LIBERADO; nenhuma execução anterior esperando resposta; campo e placeholders obrigatórios completos; etapa compatível.

Entrada → marcar modo BOT e módulo → verificar campos já conhecidos → enviar uma pergunta → aguardar → escolha exata atualiza apenas o dado correspondente → salvar checkpoint → escolher próximo nó. Outra resposta → modo HUMANO, tarefa “Revisar resposta e continuar do checkpoint”, mensagem interna para Giulia → Parar Salesbot.

Não enviar nenhum colchete literal. Para campos editoriais como [RESUMO CURTO DO QUE ELE DISSE], a substituição é humana. Bloquear mensagem se faltar conteúdo. “Resumo aprovado” vazio impede a 010; Giulia pode preparar uma apresentação adequada para cumprimento isolado, sem inventar resumo.

Pedido de parada: botão “Não receber” ou comando exato previamente definido → Não contatar = sim; modo BLOQUEADO; pendência nenhuma; tarefa de revisar/encerrar → mensagem 008 → Parar. Pedidos com outras palavras entram em revisão humana sem novo disparo. O encerramento comercial pode ser concluído manualmente.

Intervenção: Giulia para a execução, marca HUMANO e resolve a tarefa. Retomada: confere histórico, atualiza campos, marca LIBERADO e inicia o módulo adequado manualmente. Não retomar automaticamente de uma resposta atrasada a menu antigo.

## 6. Menus novos da adaptação

Acrescentar os botões à pergunta existente quando forem suficientes. O texto extra só entra quando necessário para deixar inequívoca a escolha. Fallback numérico deve reproduzir os mesmos rótulos.

| Menu | Texto de apoio novo | Escolhas / efeito |
|---|---|---|
| UI-ROTA | Hoje, qual destas situações descreve sua captação? | Anuncio hoje → anuncia; Já anunciei e parei → parou; Nunca anunciei → nunca |
| UI-LADO | Qual frente você quer captar agora? | Trabalhadores → reclamante; Empresas → empresarial; Ambos → misto |
| UI-ENTENDE | Você já conhece o funcionamento básico dos anúncios pagos? | Conheço → declaração sim; Quero entender → explicar; Prefiro conversar → HUMANO |
| UI-COLETA | Como prefere completar essas informações? | Formulário → oferta; WhatsApp → HUMANO; Depois → HUMANO para combinar data |
| UI-ACEITE | Posso enviar o formulário? | Pode enviar → link; Pelo WhatsApp → HUMANO; Agora não → HUMANO |
| UI-CONVITE | Faz sentido conversarmos sobre isso? | Quero agendar → horários; Tenho uma dúvida → HUMANO; Agora não → HUMANO |
| UI-HORÁRIO | Qual destes horários funciona para você? | Opção A / Opção B, preenchidas com datas reais; Outro horário → HUMANO |
| UI-REAGENDAR | Você quer remarcar? | Quero remarcar → HUMANO; Depois → HUMANO; Não quero → encerrar pendência |

“Já anunciei” sozinho não prova que parou: classificar como parou somente pela escolha completa “Já anunciei e parei”. Botões registram autodeclaração; relatos contraditórios vão para revisão.

## 7. Módulos e nós do construtor

Cada linha abaixo define uma sequência; cada seta é um próximo passo no editor. H é passagem humana, R é ramo resposta, T é ramo tempo esgotado. Escolher apenas uma variante por condição; nunca enviar todas as alternativas.

### SB00 — Ativação e retorno inicial

Gatilho manual por lead validado; não iniciar pelo simples fato de importar a lista.

A0 guarda → A1 escolher 001 se anúncio confirmado, 003 se empresarial confirmado, senão 002 → A2 registrar data/pendência abertura → A3 Pausa (resposta ou prazo D+2 útil).

R → cancelar abertura, etapa Conversa e qualificação → H para interpretar a primeira resposta e preparar 010. T → confirmar elegibilidade e 004 → Pausa por resposta; sem resposta, encerrar essa cadência e criar tarefa de decisão, sem disparo adicional. Intermediário → H com 005/006 disponíveis. Origem do número → H com 007 e origem real preenchida.

### SB01 — Apresentação e conhecimento de anúncios

Início manual após revisão da resposta. P0 verificar Resumo aprovado → P1 enviar 010 → P2 se entendimento desconhecido, enviar 134 com UI-ENTENDE; se conhecido, pular.

Conheço → registrar declaração e encerrar módulo para próximo gatilho humano. Quero entender → 135 literal → 136, se aplicável → H para dúvida ou confirmação do entendimento. Prefiro conversar/Outra resposta → H. Não classificar entendimento pelo simples “sim” fora do menu atual.

### SB02 — Janela de Ouro e foco

Giulia escolhe pacote no lançamento: Padrão 011 + uma variação 012/013/014; Alternativo 015-A + somente 015-B1 ou 015-B2, conforme rota confirmada. Não empilhar os dois pacotes. 017 é opcional por decisão humana e calendário da campanha.

J0 confirmar período/rota → J1 enviar pacote selecionado → J2 se lado desconhecido, UI-LADO com 018; se já conhecido, pular → J3 pergunta aplicável 019/020, 021/022 ou 023 → Pausa → qualquer relato livre H. Menu exato salva lado, mas não extrai tese.

Sem resposta à pergunta de foco: cadência 123 e 124 com duas horas úteis entre contatos; 125 é alternativa de contexto/encerramento escolhida por Giulia, não terceiro disparo automático. Usar tarefa se não houver cálculo confiável de horas úteis.

### SB03 — Contexto mínimo e coleta assistida

Lançamento humano seleciona a próxima pergunta que falta. 024/025 identificam fonte; 026/027 para atuais; 028/029 para quem parou; 030/031 para nunca; 032 para satisfeito. Relato livre → H.

Submódulos curtos: verba atual 137 ou histórica 138; plataforma 139; intenção/tese 140; atendimento 035; capacidade 036; momento 037. Um submódulo envia uma pergunta e para na resposta para revisão. Giulia preenche campos e decide seguinte, reaproveitando tudo já informado.

141–144 somente com referência comercial atual e intervenção humana. Não converter faixa de orçamento ou causa em diagnóstico automático. Contexto validado só Giulia marca. Se sem tempo e objetivo/interesse claros, Giulia libera formulário com lacunas registradas. Não impor interrogatório antes dele.

### SB04 — Oferta e envio de formulário

F0 Contexto validado ou exceção humana documentada → F1 145 para anuncia/parou ou 146 para nunca → F2 147 com UI-ACEITE → Pausa.

Pode enviar → checar URL do próprio lead → 148 → status enviado + data + pendência formulário → iniciar espera/cadência de SB05. WhatsApp → 044 ou 075, conforme situação → coleta WhatsApp → H. Agora não/Outra resposta → H.

149 para falta de tempo exige seleção humana; 150 quando dados suficientes dispensa formulário e abre tarefa de devolutiva. 045 é resposta humana ao pedido prematuro de reunião.

### SB05 — Formulário pendente e recebimento

Cadastro do recebimento deve atualizar o mesmo lead por identificação confiável; não criar outro negócio. Confirmar conclusão manualmente no MVP. Webhook/API (integração por eventos, sem IA) é evolução opcional.

Recebido → parar espera ativa, status recebido, pendência nenhuma → 046 apenas com prazo real → tarefa “Giulia: construir primeira leitura” → HUMANO → Parar. “Já preenchi” sem confirmação → H, não recebido automático. 047 somente com novo prazo aprovado.

D+1 158; D+3 159; D+5 160. Cada envio condicionado a status enviado, sem resposta nova, sem modo HUMANO/BLOQUEADO e sem preenchimento confirmado. Resposta em qualquer ramo → cancelar cadência e H; escolha WhatsApp → coleta WhatsApp e H. Não detectar iniciado/abandonado sem dados do formulário. Não enviar uma cobrança final se já houve manifestação de interesse em continuar por outro caminho.

### SB06 — Devolutiva e convite

Início manual. D0 Devolutiva aprovada e texto final disponível → Giulia envia a composição baseada em 048, ou bot envia somente o texto aprovado → registrar entrega confirmada → convite 151 (correção) ou 152 (construção) com UI-CONVITE, apenas se reunião aprovada → Pausa.

Quero agendar → interessado, pendência reunião → SB07. Dúvida/Agora não/Outra resposta → H. Sem resposta → 130 D+1 e 131 D+3; encerrar convite. 049/050 são exemplos simulados e nunca saídas automáticas. 051 depende da lacuna escolhida por Giulia. 054 se recusa reunião, com aprovação humana.

### SB07 — Agendamento e lembrete

Gatilho humano após disponibilidade real. 153/154 para iniciar escolha, 055/056 com UI-HORÁRIO quando aplicáveis; não enviar variantes redundantes.

Escolha → tarefa “Confirmar disponibilidade e criar evento” → H. Marcar só depois da confirmação no calendário; tarefa não equivale a evento. 057–061 conforme dados completos e ações efetivamente feitas. Link e convite precisam existir antes da mensagem correspondente.

Confirmação manual/integração registra data/link/status marcada, cancela convite. 062 com reunião ainda marcada e no horário parametrizado; configurar tarefa de envio no MVP. No-show confirmado por Giulia → 063/UI-REAGENDAR; D+3 sem resposta cria tarefa de encerramento, não inventar nova mensagem aprovada. Realizada → H com resultado registrado, oferta indicada ou encerramento.

### SB08 — Proposta e formalização

Proposta preparada e valores aprovados por Giulia → 102/103 conforme contexto, URL e data reais → pendência proposta → esperar.

Aceite, desconto, sócio, dúvida e qualquer texto livre → H. Não classificar “sim” como aceite contratual. 104/105 na data combinada; sem data, 132 D+3 e 133 D+7. 106–111 e 101 são biblioteca para negociação humana.

Aceite confirmado → Formalização → 112 com condições aprovadas. 113/114 só na data combinada e depois de verificar assinatura/pagamento. Ganho apenas após critério de contratação definido por Giulia e confirmado; então 115. Não marcar ganho porque uma mensagem foi enviada.

### SB09 — Encerramento e reativação

116/117 para falta de encaixe/orçamento, escolhidas por Giulia. 118/119 para combinar retomada; data real gera tarefa. 120/121 somente na retomada aprovada. 122 para recusa definitiva. Não contatar bloqueia reativação. Silêncio não vira reciclagem infinita.

### SB10 — Dúvidas e objeções

Mensagens 064–088 e 155–157 disponíveis para escolha humana por assunto. Não roteá-las automaticamente por palavra solta. Para pergunta explícita sobre funcionamento, o humano pode iniciar módulo 135; para valores, selecionar 067/068 somente com oferta atual preenchida. Nunca substituir objeção contextual por resposta padrão automática.

## 8. Cadências e cancelamento

| Pendência | Prazos desde D0 | Mensagens | Condição final |
|---|---|---|---|
| Abordagem | D+2 útil | 004 | Encerrar sequência |
| Foco | +2h úteis e mais 2h úteis | 123 / 124 | Encerrar; 125 só variante humana |
| Oferta da leitura | D+1 e D+3 úteis | 126 / 127 | Encerrar oferta pendente |
| Formulário | D+1, D+3, D+5 úteis | 158 / 159 / 160 | Encerrar pendência |
| Convite | D+1 e D+3 úteis | 130 / 131 | Encerrar convite |
| No-show | Após horário e D+3 útil | 063 / tarefa | Revisão humana |
| Proposta | Data combinada; senão D+3 e D+7 úteis | 104/105 OU 132/133 | Encerrar acompanhamento |
| Formalização | Data combinada | 113/114 | Conferir situação real |

Dias úteis não equivalem a cronômetros de 24/48 horas. **MVP recomendado:** criar tarefa com data útil correta e executar retomada manualmente. **Automação completa:** calendário determinístico calcula vencimentos e retorna evento ao Kommo; sem IA, mas com integração. Horário ativo do bot não prova contagem de dias úteis/feriados. Se configurar relógios nativos, validar sexta-feira, fim de expediente e feriado antes de liberar.

Sempre há próxima ação: uma tarefa humana ou espera do bot registrada em SB pendência. Ao encerrar espera sem outra ação, criar tarefa de decisão. Não completar indiscriminadamente todas as tarefas do lead: cancelar apenas as da cadência correspondente, por tipo/identificador testado; se o editor não permitir seletividade, Giulia conclui manualmente.

Cancelar no primeiro evento: resposta; mudança para HUMANO; não contatar; formulário recebido; reunião marcada; proposta decidida; formalização concluída; perda/ganho. Eventos externos devem parar a execução antiga antes de lançar outra. No MVP isso é manual. Atualizar um campo sozinho não garante que um bot em pausa foi encerrado.

Cada envio deve repetir a guarda final. Se o conector não expuser última resposta/execução, não alegar proteção automática: desabilitar o envio automático daquele caso e usar tarefa. Data de última resposta, quando disponível, precisa ser comparada ao início da pendência; resposta antiga não conta. Prazos não se reiniciam a cada follow-up.

## 9. Construção no Kommo e checklist de liberação

1. Criar um funil e os campos; responsável Giulia; grupo técnico separado.
2. Conferir conector, plano e disponibilidade dos passos, botões e variáveis.
3. Cadastrar textos do catálogo como modelos, conservando IDs. Importação em massa não é presumida.
4. Construir SB00, passagem humana e bloqueio antes de construir menus avançados.
5. Construir SB01/SB02; depois coleta por submódulos e SB04.
6. Implementar confirmação manual do formulário e SB06; depois agendamento/proposta.
7. Manter gatilhos manuais no MVP. Não ligar “mensagem recebida” a todos os bots nem ativar a base inteira.
8. Liberar follow-ups por tarefas; só automatizar após validar cancelamentos e calendário.
9. Testar com leads fictícios e número de teste; depois lote pequeno real revisado.

**Testes de aceite:** caminho anuncia/parou/nunca; reclamante/empresarial/misto; dado já preenchido; resposta livre; áudio; resposta dupla; “não tenho agência”; pedido de parar; botão fora de contexto; resposta após primeiro follow-up; formulário concluído durante espera; reunião marcada durante espera; Giulia assumindo; bot concorrente; falha de entrega; placeholder vazio; sexta-feira/feriado; proposta aceita sem contrato; reativação bloqueada.

Critério: nenhuma mensagem sem variável; nenhuma classificação por inferência; nenhuma cobrança depois de resposta/conclusão confirmada; nenhuma promessa artesanal feita pelo bot; exemplos e roteiro da call fora do chatbot. Se a proteção não passar no teste, manter a ação humana.

## 10. Fontes técnicas oficiais

Consultadas em 10/10/2026. Recursos podem depender da conta/conector; nenhum login ou configuração da conta foi realizado nesta entrega.

- [Salesbot: visão geral](https://support.kommo.com/docs/pt-br/salesbot-overview)
- [Criação e gatilhos](https://support.kommo.com/docs/create-a-salesbot-in-kommo)
- [Gatilhos do Salesbot](https://support.kommo.com/docs/configure-your-salesbot-triggers)
- [Interrupções entre Salesbots](https://support.kommo.com/docs/manage-salesbot-interruptions)
- [Parar bot por API, para integração opcional](https://developers.kommo.com/reference/stop-salesbot)

## 11. Catálogo literal de mensagens e permissão de uso

As 146 mensagens da base estão abaixo, com a atualização explícita da 011. IDs ausentes não devem ser recriados. 009 e 04.4 continuam removidos; 015-A/B1/B2 continuam separados. 134 e 135 preservadas. Este catálogo não é uma fila de disparos.

Legenda: **H** = somente seleção/preenchimento humano; **B** = elegível para módulo determinístico com guardas; **X** = referência, proibida como saída automática. Mensagens com placeholders editoriais exigem preparação humana mesmo quando B. Menus UI são complementos, não reescritas.

### MENSAGEM 001 — B

~~~text
*Dr. [NOME], vi que vocês já trabalham [TESE OBSERVADA] nos anúncios e fiquei com uma dúvida:*

Hoje, os contatos que chegam têm o perfil de caso que vocês procuram ou ainda entra bastante gente desqualificada?
~~~

### MENSAGEM 002 — B

~~~text
*Dr. [NOME], vi que você atua no Direito Trabalhista e fiquei com uma dúvida:*

Hoje, como vocês fazem a captação de novos reclamantes e/ou reclamadas?
~~~

### MENSAGEM 003 — B

~~~text
Dr. [NOME], vi que vocês atuam no trabalhista empresarial.

Hoje, os novos clientes dessa frente chegam principalmente por indicação ou vocês já usam o digital para atrair empresas?
~~~

### MENSAGEM 134 — B

~~~text
Você já anunciou ou impulsionou algum post? Ou sabe como funciona?
~~~

### MENSAGEM 135 — B

~~~text
*A Metha monta a operação de captação com estratégia própria, conhecimento técnico, configurações, infraestrutura e atendimento estruturado. Depois, gerencia essa operação por um valor mensal.*

A verba dos anúncios é separada e cobrada pelo Google ou Meta (Instagram/Facebook) diretamente na sua conta de anunciante. *Esse dinheiro não passa pela Metha.*
~~~

### MENSAGEM 136 — B

~~~text
É esse tipo de captação que você quer avaliar para o escritório?
~~~

### MENSAGEM 004 — B

~~~text
Dr. [NOME], é você quem acompanha essa parte de captação do escritório?
~~~

### MENSAGEM 005 — H

~~~text
Sou a Giulia, da Metha Jurídica. O assunto é a captação de clientes trabalhistas do escritório.
~~~

### MENSAGEM 006 — H

~~~text
Quem costuma acompanhar essa parte por aí?
~~~

### MENSAGEM 007 — H

~~~text
Encontrei este contato em [FONTE REAL]. Sou a Giulia, da Metha Jurídica, e te procurei por causa da atuação trabalhista do escritório.
~~~

### MENSAGEM 008 — B

~~~text
Entendido. Vou encerrar o contato por aqui.
~~~

### MENSAGEM 010 — B

~~~text
Entendi. Hoje vocês [RESUMO CURTO DO QUE ELE DISSE].

Bom, prazer! Sou da Metha, Especializada em Captação TRABALHISTA  como a do Dr. Giancarlo, que atua no trabalhista empresarial:
https://www.instagram.com/p/DPUqjcwjo0g
~~~

### MENSAGEM 011 — B

~~~text
*E te chamei agora por um motivo:* estamos entrando na *JANELA DE OURO do trabalhista: pré-recesso, recesso e pós-recesso*.

O escritório entra em recesso. O problema trabalhista dos trabalhadores continuam/aumentam

*Quando outros escritórios pausam os anúncios ou reduzem o ritmo, aparecem menos para pessoas e empresas que continuam procurando ajuda.* Quem segue visível e pronto para atender tem a oportunidade de receber contatos que eles deixam passar.

*É esse o oceano azul: aparecer, atender e disputar os contratos que os escritórios em pausa deixam de disputar.*

O ponto é estar com a tese, a comunicação e o atendimento preparados para aproveitar esse espaço.
~~~

### MENSAGEM 012 — B

~~~text
*Quem procura um advogado agora quer resolver um problema, não esperar o seu calendário.*

Enquanto um escritório adia a captação, outro pode estar ouvindo esse cliente e disputando o contrato.

*O cliente que você deixa de alcançar agora não fica reservado para janeiro.*
~~~

### MENSAGEM 013 — B

~~~text
*A vantagem do concorrente começa antes do contrato: começa quando ele atende primeiro.*

Se você espera a retomada para aparecer, pode encontrar o cliente que queria já em conversa com outro escritório.

*Quando você começa a captar, ele pode já estar escolhendo quem contratar.*
~~~

### MENSAGEM 014 — B

~~~text
*A placa de “recesso” fecha a porta do escritório. Não fecha o problema de quem precisa de advogado.*

Se a sua captação também para, você deixa de disputar essa oportunidade enquanto ela existe.

*O cliente segue procurando. A questão é qual escritório ele vai encontrar.*
~~~

### MENSAGEM 015-A — B

~~~text
*Te chamei agora porque estamos entrando na JANELA DE OURO da captação trabalhista: pré-recesso, recesso e pós-recesso.*

*Quando um escritório pausa a captação, o potencial cliente não pausa o problema.* Ele continua precisando de ajuda — e pode encontrar quem segue visível e pronto para atender.

É nessa diferença que está o *oceano azul*: aproveitar o espaço que outros escritórios deixam quando reduzem o ritmo.
~~~

### MENSAGEM 015-B1 — B

~~~text
Para quem já anuncia e está com a captação fraca, é oportunidade de *corrigir o que trava a entrada dos casos desejados e buscar contratos agora.*

*Onde outros veem pausa, a gente enxerga espaço para fechar contratos antes de 2027 com captação, tese e atendimento trabalhando na mesma direção.*
~~~

### MENSAGEM 015-B2 — B

~~~text
Para quem depende de indicação e de ser percebido no Instagram, é oportunidade de *começar uma captação direcionada pela tese que quer trabalhar.*

*Onde outros veem pausa, a gente enxerga espaço para fechar contratos antes de 2027 com captação, tese e atendimento trabalhando na mesma direção.*
~~~

### MENSAGEM 016 — H

~~~text
*Para quem já anuncia e está insatisfeito, essa janela é de correção. Para quem ainda depende de indicação e Instagram, é de construção.*

Nos dois casos, o objetivo é sair do “vamos ver o que chega” e trabalhar a entrada do tipo de cliente que o escritório quer.
~~~

### MENSAGEM 017 — H

~~~text
*A ideia é usar outubro, novembro e dezembro para buscar contratos ainda este ano e entrar em 2027 com uma carteira em formação e uma operação mais ajustada.*

Essa carteira pode gerar honorários nos próximos meses, inclusive em dezembro ou janeiro quando o caso e a forma de pagamento permitirem — por exemplo, em acordos.

Se deixar tudo para janeiro, você ainda começa escolhendo tese, montando campanha e ajustando atendimento. Depois vem o Carnaval.

> Quando percebe, é março e uma parte do primeiro trimestre foi consumida na preparação.
~~~

### MENSAGEM 018 — B

~~~text
Hoje vocês querem crescer mais com reclamantes ou com empresas?
~~~

### MENSAGEM 019 — B

~~~text
Qual tese trabalhista vocês gostariam que chegasse mais hoje?
~~~

### MENSAGEM 020 — B

~~~text
Dentro do trabalhista, tem algum tipo de caso que faz mais sentido para vocês priorizarem?
~~~

### MENSAGEM 021 — B

~~~text
Que perfil de empresa vocês gostariam de atrair para essa frente?
~~~

### MENSAGEM 022 — B

~~~text
E o foco seria mais consultivo, defesa em processos ou contratos recorrentes?
~~~

### MENSAGEM 023 — B

~~~text
Se fosse para priorizar uma dessas frentes agora, qual teria mais importância para o escritório?
~~~

### MENSAGEM 024 — H

~~~text
Essa captação hoje vem de anúncios ou principalmente de indicação e outras fontes?
~~~

### MENSAGEM 025 — H

~~~text
Você já chegou a investir em anúncios ou ainda não testou essa frente?
~~~

### MENSAGEM 026 — H

~~~text
O que mais incomoda hoje nos contatos que chegam pelos anúncios?
~~~

### MENSAGEM 027 — H

~~~text
Entendi. Você quer mais [TIPO DE CASO OU CLIENTE], mas hoje [PROBLEMA RELATADO].

Essa diferença é o que vale olhar primeiro.
~~~

### MENSAGEM 028 — H

~~~text
Qual foi o principal motivo para você parar?
~~~

### MENSAGEM 029 — H

~~~text
Entendi. Antes de pensar em retomar, vale separar o que aconteceu naquela tentativa do que precisaria mudar agora.
~~~

### MENSAGEM 030 — H

~~~text
O que você gostaria de mudar na captação que tem hoje?
~~~

### MENSAGEM 031 — H

~~~text
Entendi. Você quer uma segunda fonte de [PERFIL DE CLIENTE], além do que já chega por [FONTE ATUAL].

O primeiro passo é entender por onde começar e se o escritório consegue atender essa demanda.
~~~

### MENSAGEM 032 — H

~~~text
Entendi. Existe algum tipo de caso ou resultado que vocês ainda gostariam de desenvolver mais?
~~~

### MENSAGEM 137 — B

~~~text
Hoje vocês colocam mais ou menos quanto por mês nos anúncios, só de verba paga à plataforma?
~~~

### MENSAGEM 138 — B

~~~text
Quando anunciavam, colocavam mais ou menos quanto por mês na plataforma, fora o valor da agência, se havia uma?
~~~

### MENSAGEM 139 — B

~~~text
Esses anúncios eram no Google, no Instagram/Facebook ou em outro lugar?
~~~

### MENSAGEM 140 — B

~~~text
Que tipo de caso ou cliente vocês estavam tentando atrair com esses anúncios?
~~~

### MENSAGEM 035 — B

~~~text
Quem costuma atender os novos contatos quando eles chegam?
~~~

### MENSAGEM 036 — B

~~~text
Hoje vocês conseguiriam absorver novos casos sem comprometer o atendimento ou precisariam ajustar alguma coisa antes?
~~~

### MENSAGEM 141 — H

~~~text
Para você ter uma referência: o projeto de entrada para uma tese no Instagram/Facebook é de R$ 1.189 por mês pelo trabalho da Metha, mais a verba dos anúncios, recomendada a partir de R$ 1.200 por mês.

Isso soma R$ 2.389 por mês nessa referência, em um projeto de seis meses. O escopo depende do que o escritório precisa.
~~~

### MENSAGEM 142 — H

~~~text
Para uma frente no Google, a referência é o projeto Crescimento: R$ 1.689 por mês pelo trabalho da Metha, mais a verba dos anúncios, recomendada a partir de R$ 1.200 por mês.

Isso soma R$ 2.889 por mês nessa referência, em um projeto de seis meses. O escopo depende do seu cenário.
~~~

### MENSAGEM 143 — H

~~~text
Essa ordem de investimento está dentro do que você considera viável para a captação agora?
~~~

### MENSAGEM 144 — H

~~~text
Nos três últimos meses completos, vocês fecharam aproximadamente quantos novos contratos trabalhistas ao todo?
~~~

### MENSAGEM 037 — B

~~~text
Você quer trabalhar isso agora ou ainda está avaliando para mais adiante?
~~~

### MENSAGEM 145 — B

~~~text
Pelo que você me contou, vocês querem [TIPO DE CASO OU CLIENTE], mas [PROBLEMA RELATADO].

Para organizar essa análise, vou completar os pontos que faltam em um formulário. Com essas informações, te devolvo por aqui uma primeira leitura do cenário e o que eu priorizaria para aproximar a captação desse objetivo.
~~~

### MENSAGEM 146 — B

~~~text
Pelo que você me contou, o objetivo é começar a atrair [TIPO DE CASO OU CLIENTE], além de [FONTE ATUAL].

Para organizar essa análise, vou completar os pontos que faltam em um formulário. Depois te devolvo por aqui uma primeira leitura do cenário e o que eu priorizaria para começar essa frente no seu escritório.
~~~

### MENSAGEM 147 — B

~~~text
Te envio o formulário para completar esses pontos?
~~~

### MENSAGEM 148 — B

~~~text
Aqui está: [LINK DO FORMULÁRIO]

Ele organiza o que falta para essa primeira leitura. O retorno será por aqui no WhatsApp.
~~~

### MENSAGEM 149 — H

~~~text
Para não depender de várias respostas ao longo do dia, podemos organizar o que falta no formulário e você preenche quando puder. Depois te devolvo por aqui a primeira leitura e a prioridade para [OBJETIVO].
~~~

### MENSAGEM 150 — B

~~~text
Com o que você já me contou, tenho base para organizar essa primeira leitura.

Vou te devolver por aqui o que enxerguei e a prioridade para [OBJETIVO] até [DIA E HORÁRIO].
~~~

### MENSAGEM 044 — B

~~~text
Podemos completar por aqui. Vou aproveitar o que você já me contou e perguntar só o que falta para fazer a primeira leitura.
~~~

### MENSAGEM 045 — H

~~~text
Podemos conversar. Antes, vou organizar a primeira leitura do seu cenário para a reunião já ter uma pauta útil.
~~~

### MENSAGEM 046 — B

~~~text
Recebi suas respostas, Dr. [NOME].

Vou olhar o cenário e te devolver a primeira leitura até [DIA E HORÁRIO].
~~~

### MENSAGEM 047 — H

~~~text
Dr. [NOME], preciso ajustar o prazo da sua primeira leitura para [NOVO DIA E HORÁRIO].

Quero organizar [PONTO REAL] com cuidado. Te devolvo por aqui nesse horário.
~~~

### MENSAGEM 048 — H

~~~text
Dr. [NOME], analisei o que você me passou.

O ponto mais importante é [FATO RELATADO].

Minha hipótese inicial é [EXPLICAÇÃO POSSÍVEL]. Eu começaria por [PRIORIDADE CONCRETA], porque [MOTIVO].

Para confirmar isso, ainda precisaria olhar [INFORMAÇÃO OU MATERIAL].
~~~

### MENSAGEM 049 — X

~~~text
Dr. [NOME], analisei o que você me passou.

Você quer mais casos de acidente de trabalho, mas relata que boa parte dos contatos procura orientação trabalhista genérica.

Minha primeira hipótese é que a comunicação ou as buscas que trazem essas pessoas estejam amplas demais para esse objetivo.

Eu começaria comparando as buscas que geraram os contatos com o que o anúncio e a página apresentam. Antes de aumentar a verba, vale verificar se ela está chegando ao público que você quer.

Sem olhar esses materiais, ainda não dá para afirmar onde está a causa.
~~~

### MENSAGEM 050 — X

~~~text
Dr. [NOME], pelo que você me contou, o objetivo é atrair mais casos de [TIPO DE CASO], além das indicações.

Como você também atende os novos contatos, eu começaria definindo quais informações precisam ser coletadas antes de você fazer a análise jurídica.

Isso ajuda a preparar o atendimento antes de abrir uma nova fonte de contatos.

A escolha do canal e da verba ainda depende de olhar a região e o público que você pretende alcançar.
~~~

### MENSAGEM 051 — H

~~~text
Dr. [NOME], pelas suas respostas, está claro que você quer [OBJETIVO].

Ainda não tenho base para apontar uma causa para [PROBLEMA]. O primeiro ponto a esclarecer é [LACUNA], porque isso muda a prioridade entre [CAMINHO 1] e [CAMINHO 2].
~~~

### MENSAGEM 151 — B

~~~text
*O próximo passo é olhar como essa correção funcionaria no seu escritório.*

Em 30 minutos, eu te mostro como estruturaria [PRIORIDADE DA LEITURA] para buscar [TIPO DE CASO OU CLIENTE], com a captação por tese e o atendimento trabalhando na mesma direção.

A ideia é você entender o caminho e avaliar se a forma de trabalho da Metha faz sentido. Se houver encaixe e interesse dos dois lados, seguimos para a proposta.
~~~

### MENSAGEM 152 — B

~~~text
*O próximo passo é olhar como começar essa captação no seu escritório.*

Em 30 minutos, eu te mostro como estruturaria [PRIORIDADE DA LEITURA] para atrair [TIPO DE CASO OU CLIENTE], com a tese, os anúncios e o atendimento organizados para essa frente.

A ideia é você entender o caminho e avaliar se a forma de trabalho da Metha faz sentido. Se houver encaixe e interesse dos dois lados, seguimos para a proposta.
~~~

### MENSAGEM 153 — B

~~~text
Tenho [DIA 1] às [HORA 1] ou [DIA 2] às [HORA 2], no horário de Brasília. Qual funciona melhor para você?
~~~

### MENSAGEM 154 — B

~~~text
Faz sentido aprofundarmos essa prioridade em uma conversa de 30 minutos?
~~~

### MENSAGEM 054 — H

~~~text
Tudo bem. Você já tem a primeira leitura por aqui.

Se quiser aprofundar [PRIORIDADE] depois, seguimos de onde paramos.
~~~

### MENSAGEM 055 — B

~~~text
Tenho [DIA 1] às [HORA 1] ou [DIA 2] às [HORA 2], no horário de Brasília.

Qual fica melhor para você?
~~~

### MENSAGEM 056 — B

~~~text
Qual período costuma funcionar melhor para você?
~~~

### MENSAGEM 057 — H

~~~text
Combinado: [DIA] às [HORA], pelo Google Meet.

Vamos olhar [PAUTA ESPECÍFICA], com base na primeira análise que te enviei.
~~~

### MENSAGEM 058 — H

~~~text
Qual e-mail você prefere para receber o convite?
~~~

### MENSAGEM 059 — H

~~~text
Outra pessoa participa dessa decisão com você?
~~~

### MENSAGEM 060 — H

~~~text
Ela consegue participar desse horário também?
~~~

### MENSAGEM 061 — B

~~~text
Convite enviado. Este é o link: [LINK DO MEET]

Se surgir algum imprevisto, me avise por aqui para ajustarmos o horário.
~~~

### MENSAGEM 062 — B

~~~text
Dr. [NOME], nossa conversa sobre [PAUTA] está marcada para hoje às [HORA].

O link é este: [LINK DO MEET]. Até lá.
~~~

### MENSAGEM 063 — B

~~~text
Dr. [NOME], não conseguimos conversar no horário combinado.

Se ainda quiser olhar [PAUTA], posso te mandar novas opções.
~~~

### MENSAGEM 064 — H

~~~text
A Metha estrutura a captação para o tipo de caso trabalhista que o escritório quer receber.

Isso envolve entender o público, trabalhar os anúncios e as páginas quando necessárias, acompanhar os resultados e orientar os critérios do atendimento.

O projeto é definido a partir do que precisa mudar no seu cenário.
~~~

### MENSAGEM 065 — H

~~~text
A filtragem começa pelo que o anúncio e a página comunicam e continua nas informações levantadas no atendimento.

Os critérios mudam conforme o tipo de caso. A ideia é organizar esse contexto antes de exigir a sua análise jurídica.

A decisão sobre a viabilidade do caso continua sendo do advogado.
~~~

### MENSAGEM 066 — H

~~~text
Esse percentual depende do tipo de caso, do canal, da região e do critério que o escritório usa.

Sem olhar esse contexto, eu não te passaria uma média como se ela fosse representar o seu resultado.
~~~

### MENSAGEM 067 — H

~~~text
Os projetos começam em R$1.189 por mês, além da verba dos anúncios, recomendada a partir de R$1.200 por mês.

Essa entrada é para uma tese no Meta. O projeto Crescimento, que pode trabalhar Google ou Meta, custa R$1.689 por mês, também com a mídia à parte.

O projeto tem duração de seis meses. A indicação do escopo depende do seu cenário.
~~~

### MENSAGEM 068 — H

~~~text
Essa ordem de investimento está dentro do que você considera viável agora?
~~~

### MENSAGEM 069 — H

~~~text
Entendi. Não faz sentido mexer no que está funcionando.

A análise só vale se existir algo na captação que você queira melhorar.
~~~

### MENSAGEM 070 — H

~~~text
Existe algum resultado ou tipo de caso que você gostaria de desenvolver mais hoje?
~~~

### MENSAGEM 071 — H

~~~text
Entendo o receio de repetir um investimento que não trouxe o que você esperava.

É justamente por isso que a primeira leitura precisa olhar o que aconteceu antes de sugerir uma nova tentativa.
~~~

### MENSAGEM 072 — H

~~~text
O que mais te fez concluir que aquela tentativa não funcionou?
~~~

### MENSAGEM 155 — H

~~~text
Podemos organizar o que falta no formulário para você responder quando puder, sem depender de várias mensagens durante o dia. Depois te devolvo a primeira leitura por aqui.
~~~

### MENSAGEM 074 — H

~~~text
Você já tem a prioridade inicial por aqui. Se quiser aprofundar depois, podemos combinar um horário que funcione para você.
~~~

### MENSAGEM 075 — H

~~~text
Podemos completar por aqui. Vou aproveitar o que você já me contou e perguntar só o que falta para fazer a primeira leitura.
~~~

### MENSAGEM 156 — H

~~~text
A primeira leitura é entregue por aqui e não depende de contratar ou agendar reunião. Ela traz o que enxerguei nas informações e uma orientação sobre a prioridade; não é um diagnóstico completo da operação.
~~~

### MENSAGEM 077 — H

~~~text
Posso te passar os valores de referência. Para montar a proposta com o escopo certo, preciso definir o que ela deve resolver.

Vou aproveitar o que você já me contou para fechar essa primeira leitura.
~~~

### MENSAGEM 157 — H

~~~text
Entendi. O ponto é que [PROBLEMA RELATADO] não muda com a virada do calendário.

*Janeiro pode ser o mês de continuar uma captação já corrigida ou o mês de começar a descobrir o que precisa mudar.*

A primeira leitura te dá uma prioridade agora, para você decidir a execução com mais clareza.
~~~

### MENSAGEM 079 — H

~~~text
Entendi. Se começar significa montar tudo em janeiro, você ainda precisa escolher tese, canal e atendimento antes de aprender com a captação.

*A Janela de Ouro é a chance de começar esse aprendizado antes e buscar contratos já nos próximos meses, em vez de adiar de novo até depois do Carnaval.*

A primeira análise pode mostrar qual seria o ponto de partida para o seu escritório.
~~~

### MENSAGEM 080 — H

~~~text
Eu não partiria da ideia de que a demanda vai subir em toda tese.

*A oportunidade também pode estar na concorrência:* se outros escritórios reduzem os anúncios e ainda existe procura pelo tipo de caso que você atende, pode abrir espaço para disputar essa demanda.

Por isso a nossa leitura parte da tese e da região, com atendimento preparado para quem chegar. O recesso, por si só, não decide se essa captação faz sentido.
~~~

### MENSAGEM 081 — H

~~~text
Pode acontecer, conforme os contratos que forem fechados e a forma de pagamento de cada caso — inclusive por acordo, quando for o caso.

*Nosso trabalho é desenvolver a entrada e o atendimento de oportunidades. A data dos honorários depende também do caso e da contratação jurídica.*

A ideia é começar a construir essa carteira agora e trabalhar a performance ao longo de 2027.
~~~

### MENSAGEM 082 — H

~~~text
Posso te mostrar um exemplo de um escritório com um contexto próximo ao seu, para você entender como esse trabalho foi pensado.
~~~

### MENSAGEM 083 — H

~~~text
Quer que eu te envie?
~~~

### MENSAGEM 084 — H

~~~text
Não consigo garantir contratos ou faturamento.

O que precisa ficar definido é o trabalho contratado, o acompanhamento, os critérios de qualidade e como vamos avaliar os resultados.
~~~

### MENSAGEM 085 — H

~~~text
Entendi. Então aumentar volume pode nem ser a prioridade.
~~~

### MENSAGEM 086 — H

~~~text
Vocês gostariam de receber um perfil diferente de caso ou estão satisfeitos com a carteira atual?
~~~

### MENSAGEM 087 — H

~~~text
Esse exemplo mostra o que aconteceu naquele contexto.

O que ajuda na comparação com você é [SEMELHANÇA REAL]. A diferença que precisamos considerar é [DIFERENÇA REAL].
~~~

### MENSAGEM 088 — H

~~~text
A tecnologia pode ajudar a organizar os contatos, coletar informações iniciais e acompanhar as próximas ações.

Na Metha, a Lawria é opcional e tem contratação separada. Ela não entra automaticamente no valor da assessoria.

A análise jurídica e a decisão sobre o caso continuam com o advogado.
~~~

### MENSAGEM 089 — X

~~~text
Dr. [NOME], obrigada pelo seu tempo.

Eu já organizei a primeira leitura que te enviei. Hoje quero aprofundar [PONTO], te mostrar como eu pensaria esse caminho no seu escritório e entender se há encaixe para trabalharmos juntos.

Você não precisa tomar uma decisão de contratação nesta conversa.
~~~

### MENSAGEM 090 — X

~~~text
Essa pauta atende o que você gostaria de esclarecer hoje?
~~~

### MENSAGEM 091 — X

~~~text
Pelo que você me contou, hoje [SITUAÇÃO], você quer [OBJETIVO] e o principal ponto a resolver é [PROBLEMA].
~~~

### MENSAGEM 092 — X

~~~text
Tem algo importante que mudou ou que eu não considerei nessa leitura?
~~~

### MENSAGEM 093 — X

~~~text
Minha hipótese inicial é [HIPÓTESE]. O que me levou a ela foi [FATO OU EVIDÊNCIA].

Para confirmar, eu olharia [MATERIAL OU INDICADOR]. Sem isso, eu não trataria essa hipótese como causa fechada.
~~~

### MENSAGEM 094 — X

~~~text
Quando acontece [SITUAÇÃO RELATADA], o que vocês fazem hoje?
~~~

### MENSAGEM 095 — X

~~~text
No seu cenário, eu começaria por [PRIORIDADE].

Depois trabalharia [SEGUNDA ETAPA], para [FINALIDADE].

O que observaríamos para saber se estamos avançando seria [CRITÉRIO CONCRETO].
~~~

### MENSAGEM 096 — X

~~~text
Essa sequência faz parte do Método ORDEM.

Primeiro localizamos o que precisa mudar. Depois alinhamos a comunicação, trabalhamos a captação e organizamos o caminho dos contatos até o advogado. A melhoria vem do que os dados e o atendimento mostram.
~~~

### MENSAGEM 097 — X

~~~text
Pelo cenário que alinhamos, o projeto precisaria contemplar [ESCOPO], com [CANAL] e [PRIORIDADE].
~~~

### MENSAGEM 098 — X

~~~text
Esse caminho faz sentido para o que você quer resolver agora?
~~~

### MENSAGEM 099 — X

~~~text
Posso organizar esse escopo em uma proposta com entregas, investimento e prazo para você avaliar com calma.
~~~

### MENSAGEM 100 — X

~~~text
Quer que eu prepare?
~~~

### MENSAGEM 101 — H

~~~text
Antes de ajustar valor, vale olhar se o escopo está adequado à sua prioridade.

Se precisarmos reduzir o investimento, eu verifico o que pode ser reduzido sem comprometer o que o projeto precisa resolver.
~~~

### MENSAGEM 102 — B

~~~text
Dr. [NOME], organizei a proposta com base no que alinhamos.

Ela contempla [ESCOPO RESUMIDO], com investimento de [VALOR DA ASSESSORIA] por mês, além de [VERBA DE MÍDIA] para os anúncios.

O projeto tem duração de seis meses. As entregas, os limites e as condições estão no documento: [LINK OU ARQUIVO].
~~~

### MENSAGEM 103 — B

~~~text
Qual dia faz sentido para retomarmos depois que você avaliar?
~~~

### MENSAGEM 104 — H

~~~text
Dr. [NOME], combinamos de retomar a proposta hoje.
~~~

### MENSAGEM 105 — H

~~~text
O que você precisa esclarecer para decidir se esse projeto faz sentido agora?
~~~

### MENSAGEM 106 — H

~~~text
Tudo bem.
~~~

### MENSAGEM 107 — H

~~~text
O que você ainda precisa avaliar: o investimento, o escopo ou o momento de começar?
~~~

### MENSAGEM 108 — H

~~~text
Entendi.
~~~

### MENSAGEM 109 — H

~~~text
O valor ultrapassa o orçamento que você tem hoje ou ainda não está claro o que esse escopo resolve?
~~~

### MENSAGEM 110 — H

~~~text
Claro. Podemos esclarecer juntos os pontos que ele precisar avaliar.
~~~

### MENSAGEM 111 — H

~~~text
Qual é a principal dúvida que você espera que ele tenha?
~~~

### MENSAGEM 112 — B

~~~text
Perfeito. Vamos seguir com o escopo que você aprovou.

O próximo passo é formalizar a contratação. Vou te enviar os documentos e as orientações de pagamento conforme as condições da proposta.
~~~

### MENSAGEM 113 — B

~~~text
Dr. [NOME], para concluirmos a formalização, falta [PENDÊNCIA REAL].
~~~

### MENSAGEM 114 — B

~~~text
Precisa de alguma informação para finalizar essa etapa?
~~~

### MENSAGEM 115 — B

~~~text
Dr. [NOME], contratação formalizada.

Agora vamos iniciar o projeto conforme o escopo aprovado. Vou te enviar as orientações para o diagnóstico inicial e para organizar os materiais e acessos necessários.
~~~

### MENSAGEM 116 — H

~~~text
Dr. [NOME], pelo cenário de hoje, eu priorizaria [PONTO REAL] antes de abrir uma nova frente de captação, porque [MOTIVO].

Essa é a primeira leitura que consigo te devolver com as informações atuais.
~~~

### MENSAGEM 117 — H

~~~text
Pelo investimento que você considera viável hoje, eu não indicaria este projeto agora.

Você já tem a primeira leitura por aqui. Se o cenário mudar, podemos retomar e reavaliar o escopo.
~~~

### MENSAGEM 118 — H

~~~text
Entendi. Podemos retomar quando fizer mais sentido.
~~~

### MENSAGEM 119 — H

~~~text
Em qual período você gostaria que eu voltasse a falar com você?
~~~

### MENSAGEM 120 — B

~~~text
Dr. [NOME], combinamos de retomar [ASSUNTO] neste período.
~~~

### MENSAGEM 121 — B

~~~text
O cenário mudou desde a nossa última conversa?
~~~

### MENSAGEM 122 — H

~~~text
Entendido, Dr. [NOME]. Obrigada pelo retorno. Vou encerrar por aqui.
~~~

### MENSAGEM 123 — B

~~~text
E hoje vocês querem focar mais em reclamante ou reclamada?
~~~

### MENSAGEM 124 — B

~~~text
E dentro dessa frente, tem algum perfil de caso ou cliente que vocês gostariam de priorizar?
~~~

### MENSAGEM 125 — H

~~~text
Vocês têm algo em mente para começar ou corrigir nessa janela?
~~~

### MENSAGEM 126 — B

~~~text
Dr. [NOME], essa primeira análise de [PROBLEMA OU OBJETIVO] ainda seria útil para você agora?
~~~

### MENSAGEM 127 — B

~~~text
Vou deixar essa análise em aberto por aqui. Se quiser retomar [OBJETIVO], me avise e seguimos de onde paramos.
~~~

### MENSAGEM 158 — B

~~~text
Dr. [NOME], para seguir com a primeira leitura sobre [OBJETIVO], faltam as informações do formulário que te enviei.

Se algum campo ou o acesso travou, me avise por aqui.
~~~

### MENSAGEM 159 — B

~~~text
Dr. [NOME], você ainda quer seguir com essa primeira leitura? Se o formulário ficou difícil de encaixar, podemos completar o que falta por aqui.
~~~

### MENSAGEM 160 — B

~~~text
Vou encerrar essa pendência por enquanto. Se quiser retomar a leitura de [OBJETIVO], me avise e aproveitamos o que você já me contou.
~~~

### MENSAGEM 130 — B

~~~text
Dr. [NOME], você prefere aprofundar [PRIORIDADE DA ANÁLISE] agora ou deixar essa conversa para outro momento?
~~~

### MENSAGEM 131 — B

~~~text
Vou deixar o convite em aberto. A primeira leitura já está por aqui e podemos retomar quando fizer sentido para você.
~~~

### MENSAGEM 132 — B

~~~text
Dr. [NOME], sobre a proposta para [OBJETIVO], ficou algum ponto que você precisa esclarecer?
~~~

### MENSAGEM 133 — B

~~~text
Dr. [NOME], vou encerrar o acompanhamento desta proposta por enquanto.

Se quiser retomar, me avise. A gente confirma se o escopo e as condições continuam adequados ao seu cenário.
~~~

