"""Triagem reproduzível dos complementos, sem alterar fontes ou a matriz."""
import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]


def gerar():
    files = json.loads((ROOT / 'catalogo/arquivos.json').read_text(encoding='utf-8'))['arquivos']
    sources = [f for f in files if f['tipo'] == 'fonte']
    texts = {}
    for f in sources:
        raw = (ROOT / f['caminho']).read_bytes()
        if hashlib.sha256(raw).hexdigest() != f['sha256']:
            raise ValueError('Catálogo desatualizado: ' + f['id'])
        if Path(f['caminho']).suffix in ('.md', '.txt'):
            texts[f['id']] = re.sub(r'\s+', ' ', raw.decode('utf-8-sig')).strip()
    review = json.loads((ROOT / 'catalogo/revisao-complementos.json').read_text(encoding='utf-8'))
    decisions = {r['id']: r for r in review['revisoes']}
    rows = []
    for f in sources:
        if f['coberto_pela_matriz']:
            continue
        same_bytes = [g['id'] for g in sources if g['id'] != f['id'] and g['sha256'] == f['sha256']]
        text = texts.get(f['id'])
        same_text = [k for k, v in texts.items() if k != f['id'] and text and text == v]
        status = ('vazio' if f['bytes'] == 0 else 'identico-em-bytes' if same_bytes else
                  'mesmo-texto-sem-espacamento' if same_text else 'comparacao-editorial-pendente')
        decision = decisions.get(f['id'])
        if decision and decision['sha256'] != f['sha256']:
            raise ValueError('Revisão editorial desatualizada: ' + f['id'])
        rows.append(dict(id=f['id'], caminho=f['caminho'], sha256=f['sha256'],
                         triagem=status, identicos_em_bytes=same_bytes,
                         mesmo_texto_sem_espacamento=same_text, revisao=decision))
    if set(decisions) - {r['id'] for r in rows}:
        raise ValueError('Revisão aponta para fonte fora dos complementos')
    counts = Counter(r['triagem'] for r in rows)
    data = dict(schema_version=1, metodo='SHA-256 de todas as fontes; texto MD/TXT com espaços normalizados; sem inferência semântica.',
                total_complementos=len(rows), contagens=dict(sorted(counts.items())), arquivos=rows)
    md = ['# Triagem dos complementos', '',
          f'{len(rows)} arquivos fora da matriz; {len(decisions)} lidos integralmente nesta revisão editorial.', '',
          'Arquivos não equivalem a scripts únicos. A comparação abrange todas as fontes, inclusive as cobertas pela matriz. '
          'Hash igual comprova bytes iguais. Texto igual após normalizar espaços comprova apenas essa equivalência. '
          'Ausência de correspondência não comprova novidade. PDF, DOCX, HTML, áudio e planilha sem hash igual continuam pendentes de comparação entre formatos.', '',
          '## Revisão de dez arquivos', '',
          '| Fonte | Relação / contribuição | Encaminhamento |', '| --- | --- | --- |']
    for r in rows:
        if r['revisao']:
            d = r['revisao']
            md.append(f"| [{r['id']}](../{r['caminho']}) | {d['evidencia']} | {d['encaminhamento']} |")
    md += ['', 'Os dez arquivos foram agrupados em oito unidades editoriais de trabalho: dois pares (recesso e fechamento) e seis itens individuais. '
           'Isso organiza a amostra; não comprova oito conteúdos novos em relação às 45 fontes da matriz. '
           'Prioridade proposta: reunião → preço → follow-up; conferir sobreposição na matriz antes de extrair. '
           'Nenhuma mensagem foi acrescentada automaticamente à matriz ou aprovada para envio.', '',
           '## Todos os complementos', '', '| ID | Arquivo | Triagem | Correspondências |', '| --- | --- | --- | --- |']
    for r in rows:
        peers = sorted(set(r['identicos_em_bytes'] + r['mesmo_texto_sem_espacamento']))
        md.append(f"| {r['id']} | [{Path(r['caminho']).name}](../{r['caminho']}) | {r['triagem']} | {', '.join(peers) or 'Não comprovadas'} |")
    md += ['', 'Regerar: `python ferramentas/complementos.py atualizar`. Conferir: `python ferramentas/complementos.py validar`.', '']
    return {'catalogo/complementos.json': json.dumps(data, ensure_ascii=False, indent=2) + '\n',
            'docs/triagem-complementos.md': '\n'.join(md)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('acao', choices=['atualizar', 'validar'])
    args = parser.parse_args()
    for name, value in gerar().items():
        path = ROOT / name
        raw = value.encode('utf-8')
        if args.acao == 'atualizar':
            path.write_bytes(raw)
        elif not path.exists() or path.read_bytes() != raw:
            raise SystemExit('Triagem desatualizada: ' + name)
    print('OK: triagem de todos os complementos e revisão editorial conferidas.')


if __name__ == '__main__':
    main()
