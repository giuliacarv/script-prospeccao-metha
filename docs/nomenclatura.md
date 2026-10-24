# Organização e nomenclatura

## Critério de pasta

| Pasta | Conteúdo |
| --- | --- |
| `playbooks/` | Documentos amplos, separados pela versão declarada na fonte |
| `abordagens/` | Famílias Doug, Copydrill e Karnage, com variantes próprias |
| `scripts/whatsapp/` | Abordagem, follow-up, fechamento, funis, recesso, áudio e legado |
| `scripts/referencias/` | Repertório de origem externa ou atendimento de advocacias |
| `apoio/` | Estratégia e planilhas de objeções |
| `midias/` | Arquivos de áudio e imagem, ligados às fontes pelo catálogo |
| `modelos/kommo/v5/` | Seleção de 43 mensagens com seus IDs M |
| `matrizes/` | Matriz de comparação e documentação de cobertura |
| `catalogo/` | Registro estruturado e mapa de caminhos anteriores |
| `docs/` | Documentação e pendências; arquivos vazios ficam descritos aqui |
| `ferramentas/` | Utilitários locais de manutenção |

## Regras para novos arquivos

- Use minúsculas, sem acentos, com hífens: `perguntou-preco.md`. `README.md` é a exceção para índices de pasta.
- Preserve a extensão real e use nomes curtos. Evite símbolos, espaços, títulos inteiros e IDs de exportação no nome novo.
- Identifique versões declaradas: `v5/`, `v6.6/`, `v10/`. Uma versão maior não implica aprovação ou prioridade editorial.
- Use data ISO quando a data fizer parte clara do título original. Um timestamp de exportação não comprova data de criação.
- Preserve variantes e a identidade da origem. O título original, caminho anterior, URL e hash ficam em `catalogo/arquivos.json`.
- No V5, 00–30 preservam a ordem da exportação; não renumeram os capítulos internos do playbook.
- Não renomeie extensões para simular conversão. Se exportar um documento, registre o formato obtido e a limitação.

## Ao adicionar ou mover uma fonte

1. Escolha a pasta pela função do material e confira duplicidade por conteúdo.
2. Registre o item no JSON do catálogo, com origem e indicação de cobertura da matriz.
3. Atualize links, referências nos modelos e caminhos de arquivo na matriz quando aplicável.
4. Execute a atualização e a validação descritas em [ferramentas](../ferramentas/README.md).

O [mapa de caminhos](../catalogo/caminhos.csv) cobre os 117 arquivos que existiam antes desta reorganização. Links antigos em revisões Git continuam acessíveis no histórico. Os hashes originais permitem comparar ou recuperar o conteúdo daquela revisão.
