# Biblioteca comercial — Metha Jurídica

Scripts de prospecção, playbooks e materiais de apoio para o comercial da Metha na captação de escritórios de advocacia.

**[Catálogo completo](catalogo.md)** · **[Matriz por etapa](matrizes/mensagens-por-etapa.xlsx)** · **[43 modelos V5](modelos/kommo/v5/README.md)**

## Encontre o que precisa

| Objetivo | Onde consultar |
| --- | --- |
| Comparar mensagens por etapa da conversa | [Matriz e cobertura](matrizes/README.md) |
| Consultar o V5 exportado do Notion | [Índice V5](playbooks/v5/README.md) |
| Comparar playbooks V6.6, V6.7, V7.0, V7.2 e V8 | [Playbooks por versão](playbooks/README.md) |
| Consultar Doug, Copydrill ou Karnage | [Abordagens](abordagens/README.md) |
| Preparar abertura, follow-up, fechamento ou recesso | [Scripts de WhatsApp](scripts/README.md) |
| Revisar uma seleção para cadastro no CRM | [Modelos Kommo](modelos/kommo/v5/README.md) |
| Consultar estratégia, objeções ou mídia de referência | [Apoio](apoio/README.md) · [Áudios e imagens](midias/README.md) |
| Encontrar um nome antigo ou conferir a origem | [Mapa de caminhos](catalogo/caminhos.csv) · [Inventário](docs/inventario.md) |

## Cobertura do acervo

Há **106 arquivos de fontes**. A matriz cobre **45 documentos**, com **2.171 registros**; os **61 arquivos complementares** estão identificados no catálogo e ainda não foram extraídos para a matriz. A seleção Kommo reúne **43 mensagens** do V5.

**[Conferência dos 12 links do Drive: documento por documento](docs/cobertura-drive.md)** — inclui todas as subpastas e o destino das 63 fontes.

Uma [pendência de origem](docs/pendencias/script-janeiro-20k30d.md) registra o arquivo vazio do item 8 do Drive. O [fragmento de prospecção ativa](scripts/whatsapp/legado/prospeccao-ativa-fragmento.md) contém somente a linha disponível na fonte.

## Organização

```text
playbooks/       Versões completas e exportação V5
abordagens/      Doug, Copydrill e Karnage
scripts/        WhatsApp por situação e referências
apoio/          Estratégia e planilhas de objeções
midias/         Áudios e imagem de apoio
modelos/        Seleção editorial para Kommo
matrizes/       Planilha de mensagens e cobertura
catalogo/       Metadados, caminhos anteriores e integridade
docs/           Origem, nomenclatura e revisão do acervo
ferramentas/    Atualização de índices e validação local
```

## Como usar

1. Escolha o cenário e leia a condição de uso e o contexto completo.
2. Confira a versão e preencha os campos entre colchetes com dados reais.
3. Revise texto, oferta e provas antes de cadastrar ou enviar uma mensagem.

O acervo reúne referências editoriais, rascunhos, exemplos e variantes históricas. Termos como “final” e “validado” reproduzem a identificação da fonte; a inclusão aqui não comprova aprovação atual, eficácia comercial ou cadastro no Kommo. Scripts de atendimento jurídico e referências de terceiros estão em `scripts/referencias/`.

Os HTMLs podem ser baixados e abertos no navegador. PDFs, planilhas e mídias mantêm o formato disponível na fonte; documentos Word/Google Docs importados na etapa anterior estão em Markdown extraído. Os [detalhes da importação](docs/fontes-drive.md) registram esse limite.

## Manutenção

Os nomes usam minúsculas, hífens e caracteres compatíveis com Windows. Veja o [padrão de organização](docs/nomenclatura.md) antes de adicionar materiais.

```bash
python ferramentas/acervo.py atualizar
python ferramentas/acervo.py validar
```

A validação confere arquivos, hashes, links, nomes, blocos copiáveis, matriz e modelos. Consulte a [revisão da organização](docs/revisao-organizacao.md) para divergências de versão e evidências de preservação.
