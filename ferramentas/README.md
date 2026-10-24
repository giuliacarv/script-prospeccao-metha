# Manutenção local

Requer Python 3.10 ou superior; usa somente a biblioteca padrão. Execute na raiz do repositório:

```bash
python ferramentas/acervo.py atualizar
python ferramentas/acervo.py validar
```

`atualizar` recalcula hashes e tamanhos no JSON e gera `catalogo.md` e `docs/inventario.md`. Não descobre novas fontes automaticamente: registre o novo item no JSON antes de executar. Revise o diff do catálogo antes de publicar.

`validar` é somente leitura. Confere nomes, links locais, hashes, blocos copiáveis, mapa de caminhos, os 43 modelos e os valores das seis abas da matriz, incluindo os 2.171 IDs M. Não consulta sistemas externos nem configura o Kommo.

Se uma validação de texto ou integridade falhar, investigue a alteração antes de atualizar o valor esperado. O registro da matriz preserva o conteúdo conferido na migração; uma futura ampliação exige revisão editorial e novo registro de cobertura.
