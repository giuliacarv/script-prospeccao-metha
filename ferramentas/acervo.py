"""Atualiza índices ou valida o acervo. Python 3.10+, apenas biblioteca padrão."""
from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import posixpath
import re
import sys
import xml.etree.ElementTree as ET
import zipfile
from collections import defaultdict
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / 'catalogo/arquivos.json'
NS = {'s': 'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}
GROUPS = {
    'playbooks': 'Playbooks por versão', 'abordagens': 'Abordagens e famílias de copy',
    'scripts': 'Scripts por canal e situação', 'apoio': 'Estratégia e objeções',
    'midias': 'Áudios e imagens', 'modelos': 'Seleções para o Kommo',
    'matrizes': 'Matriz de mensagens', 'docs': 'Pendências documentadas',
    'roteiros-internos': 'Roteiros internos: originais e leituras',
}


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def write(path: str, text: str) -> None:
    dest = ROOT / path
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_bytes(text.encode('utf-8'))


def link(path: str, label: str | None = None, parent: str = '') -> str:
    target = posixpath.relpath(path, parent or '.')
    return f'[{label or path}]({target})'


def code_blocks(text: str) -> str:
    """Digest dos blocos cercados, sem depender do CRLF da máquina."""
    result, active, block = [], None, []
    for line in text.replace('\r\n', '\n').splitlines(keepends=True):
        m = re.match(r'^\s{0,3}(`{3,}|~{3,})', line)
        if active is None and m:
            active = m[1]; block = [line]
        elif active is not None:
            block.append(line)
            if re.fullmatch(r'\s{0,3}' + re.escape(active) + r'\s*', line):
                result.append(''.join(block)); active = None; block = []
    if block:
        result.append(''.join(block))
    return sha(json.dumps(result, ensure_ascii=False).encode('utf-8'))


def workbook_cells(path: Path | bytes) -> dict[str, list[list]]:
    """Lê valores e fórmulas do XLSX sem regravar estilos ou tabelas."""
    with zipfile.ZipFile(io.BytesIO(path) if isinstance(path, bytes) else path) as z:
        strings = []
        if 'xl/sharedStrings.xml' in z.namelist():
            for si in ET.fromstring(z.read('xl/sharedStrings.xml')).findall('s:si', NS):
                strings.append(''.join(t.text or '' for t in si.findall('.//s:t', NS)))
        rel = {r.attrib['Id']: r.attrib['Target'] for r in ET.fromstring(z.read('xl/_rels/workbook.xml.rels'))}
        out = {}
        for sheet in ET.fromstring(z.read('xl/workbook.xml')).findall('s:sheets/s:sheet', NS):
            rid = sheet.attrib['{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id']
            target = rel[rid]
            part = target.lstrip('/') if target.startswith('/') else posixpath.normpath('xl/' + target)
            records = []
            for cell in ET.fromstring(z.read(part)).findall('.//s:sheetData/s:row/s:c', NS):
                v, f = cell.find('s:v', NS), cell.find('s:f', NS)
                val = v.text if v is not None else None
                typ = cell.attrib.get('t', '')
                if typ == 's' and val is not None:
                    val = strings[int(val)]
                elif typ == 'inlineStr':
                    val = ''.join(t.text or '' for t in cell.findall('.//s:t', NS))
                if val is not None or f is not None:
                    records.append([cell.attrib['r'], typ, val, f.text if f is not None else None])
            out[sheet.attrib['name']] = records
        return out


def cells_digest(records: list) -> str:
    return sha(json.dumps(records, ensure_ascii=False, separators=(',', ':')).encode())


def render(data: dict) -> dict[str, str]:
    files = data['arquivos']
    sources = [f for f in files if f['tipo'] == 'fonte']
    grouped = defaultdict(list)
    for f in files:
        grouped[f['caminho'].split('/')[0]].append(f)
    catalog = ['# Catálogo do acervo', '',
               f"**{len(sources)} arquivos de fontes**, mais seleções, matriz e pendência de origem. Consulte pelo assunto, formato ou nome anterior.", '',
               'O nome original, o endereço de origem, os hashes e a cobertura da matriz constam no [JSON](catalogo/arquivos.json). '
               'O [mapa de caminhos](catalogo/caminhos.csv) permite localizar os nomes usados antes da reorganização.', '']
    for group in GROUPS:
        rows = sorted(grouped.get(group, []), key=lambda x: x['caminho'])
        if not rows:
            continue
        catalog += [f'## {GROUPS[group]}', '', '| ID | Arquivo | Formato | Matriz | Origem / observação |', '| --- | --- | --- | --- | --- |']
        for f in rows:
            origin = f"[Fonte]({f['url_origem']})" if f['url_origem'] else 'Git histórico'
            if f.get('observacao'):
                origin += ' · ' + f['observacao'].replace('|', '/')
            coverage = 'Sim' if f['coberto_pela_matriz'] else ('Derivado' if f['tipo'] == 'derivado' else 'Não')
            catalog.append(f"| {f['id']} | {link(f['caminho'])} | {Path(f['caminho']).suffix[1:].upper()} | {coverage} | {origin} |")
        catalog.append('')
    inv = ['# Inventário do acervo', '',
           'Gerado por `python ferramentas/acervo.py atualizar`. Os hashes atuais são SHA-256 dos bytes gravados. '
           'O JSON também preserva os hashes anteriores à reorganização.', '',
           f"- Fontes: **{len(sources)} arquivos**; **{sum(f['coberto_pela_matriz'] for f in sources)}** cobertos pela matriz e **{sum(not f['coberto_pela_matriz'] for f in sources)}** complementares.",
           f"- Derivados catalogados: **{sum(f['tipo']=='derivado' for f in files)}**. Pendência: **{sum(f['tipo']=='pendencia' for f in files)}**.",
           '- Identidade e conteúdo comercial são preservados por fonte; aprovação editorial é uma decisão separada.', '',
           '| ID | Arquivo | Bytes | SHA-256 atual |', '| --- | --- | ---: | --- |']
    for f in sorted(files, key=lambda x: x['caminho']):
        inv.append(f"| {f['id']} | {link(f['caminho'], parent='docs')} | {f['bytes']} | `{f['sha256']}` |")
    duplicates = defaultdict(list)
    for f in sources:
        duplicates[f['sha256']].append(f)
    inv += ['', '## Fontes idênticas em bytes', '', 'Nomes distintos foram mantidos como identidades de origem. Estes grupos contêm cópias exatas, verificadas por hash.', '']
    for digest, rows in sorted(duplicates.items()):
        if len(rows) > 1:
            inv += [f'- `{digest}`: ' + ', '.join(link(f['caminho'], f['id'] + ' · ' + f['caminho'], parent='docs') for f in rows)]
    return {'catalogo.md': '\n'.join(catalog).rstrip() + '\n', 'docs/inventario.md': '\n'.join(inv).rstrip() + '\n'}


def update() -> None:
    data = json.loads(MANIFEST.read_text(encoding='utf-8'))
    for f in data['arquivos']:
        payload = (ROOT / f['caminho']).read_bytes()
        f['sha256'], f['bytes'] = sha(payload), len(payload)
    MANIFEST.write_bytes((json.dumps(data, ensure_ascii=False, indent=2) + '\n').encode())
    for path, text in render(data).items():
        write(path, text)
    print('OK: catálogo, inventário e hashes atuais atualizados.')


def validate() -> None:
    errors = []
    import complementos
    for name, content in complementos.gerar().items():
        p = ROOT / name
        if not p.exists() or p.read_bytes() != content.encode('utf-8'):
            errors.append('Triagem desatualizada: ' + name)
    data = json.loads(MANIFEST.read_text(encoding='utf-8'))
    files = data['arquivos']
    for field in ['id', 'caminho']:
        values = [f[field] for f in files]
        if len(values) != len(set(values)):
            errors.append('Identificador repetido: ' + field)
    for f in files:
        p = ROOT / f['caminho']
        if not p.is_file():
            errors.append('Arquivo ausente: ' + f['caminho']); continue
        payload = p.read_bytes()
        if sha(payload) != f['sha256'] or len(payload) != f['bytes']:
            errors.append('Hash/tamanho divergente: ' + f['caminho'])
        if f.get('blocos_copiaveis_sha256') and code_blocks(payload.decode('utf-8-sig')) != f['blocos_copiaveis_sha256']:
            errors.append('Bloco copiável alterado: ' + f['caminho'])
    for p in ROOT.rglob('*'):
        if not p.is_file() or '.git' in p.relative_to(ROOT).parts or '__pycache__' in p.parts:
            continue
        rel = p.relative_to(ROOT).as_posix()
        canonical = rel.replace('README.md', 'readme.md')
        if not re.fullmatch(r'[a-z0-9./-]+', canonical) or len(rel) > 140:
            errors.append('Nome fora do padrão: ' + rel)
        for part in Path(rel).parts:
            if part.endswith(('.', ' ')) or re.match(r'^(con|prn|aux|nul|com[1-9]|lpt[1-9])(?:\.|$)', part, re.I):
                errors.append('Nome incompatível com Windows: ' + rel)
        if p.suffix == '.md':
            body = p.read_text(encoding='utf-8-sig')
            # Ignora exemplos de código e links multilinha já presentes nas fontes.
            body = re.sub(r'(?ms)^```[^\n]*\n.*?^```\s*$', '', body)
            for target in re.findall(r'\]\(([^)\n]+)\)', body):
                if urlsplit(target).scheme or target.startswith(('#', '/')):
                    continue
                dest = unquote(target.split('#', 1)[0])
                if not dest or '\n' in dest:
                    continue
                if not (p.parent / dest).exists():
                    errors.append(f'Link ausente em {rel}: {target}')
    for path, content in render(data).items():
        if (ROOT / path).read_bytes() != content.encode():
            errors.append('Índice desatualizado: ' + path)
    with (ROOT / 'catalogo/caminhos.csv').open(encoding='utf-8', newline='') as stream:
        rows = list(csv.DictReader(stream))
    if len({r['caminho_anterior'] for r in rows}) != len(rows):
        errors.append('Caminho anterior repetido no mapa')
    for r in rows:
        if not (ROOT / r['caminho_atual']).is_file():
            errors.append('Destino do mapa ausente: ' + r['caminho_atual'])
    models = json.loads((ROOT / 'modelos/kommo/v5/catalogo.json').read_text(encoding='utf-8-sig'))['modelos']
    with (ROOT / 'modelos/kommo/v5/catalogo.csv').open(encoding='utf-8-sig', newline='') as stream:
        model_csv = list(csv.DictReader(stream))
    if len(models) != 43 or len(model_csv) != 43 or len({m['id'] for m in models}) != 43:
        errors.append('Quantidade/IDs dos 43 modelos mudou')
    for a, b in zip(models, model_csv):
        if (a['id'], a['mensagem'], a['origem']) != (b['ID M'], b['Mensagem integral'], b['Arquivo de origem']):
            errors.append('JSON e CSV dos modelos divergem: ' + a['id'])
        if not (ROOT / a['origem']).is_file():
            errors.append('Fonte do modelo ausente: ' + a['origem'])
    wb = workbook_cells(ROOT / 'matrizes/mensagens-por-etapa.xlsx')
    expected = json.loads((ROOT / 'catalogo/matriz-integridade.json').read_text(encoding='utf-8'))
    if set(wb) != set(expected['abas']):
        errors.append('Abas da matriz divergentes')
    for name, records in wb.items():
        if cells_digest(records) != expected['abas'].get(name):
            errors.append('Conteúdo de células da matriz mudou: ' + name)
    messages = [r for r in wb.get('Mensagens integrais', []) if re.fullmatch(r'A\d+', r[0]) and re.fullmatch(r'M\d{5}', str(r[2]))]
    if len(messages) != 2171 or len({r[2] for r in messages}) != 2171:
        errors.append('Os 2.171 registros da matriz não foram preservados')
    if sum(f['coberto_pela_matriz'] for f in files) != 45:
        errors.append('Cobertura das 45 fontes mudou')
    with (ROOT / 'catalogo/cobertura-drive.csv').open(encoding='utf-8', newline='') as stream:
        coverage = list(csv.DictReader(stream))
    if len(coverage) != 64 or len({r['drive_id'] for r in coverage}) != 64:
        errors.append('Conferência dos 64 itens do Drive incompleta ou com IDs repetidos')
    for row in coverage:
        if row['status'] == 'fora-do-escopo':
            if row['nome_original'] != 'WhatsApp_RocketSend_Logs.csv' or row['caminho']:
                errors.append('Exclusão inesperada na cobertura do Drive: ' + row['drive_id'])
            continue
        dest = ROOT / row['caminho']
        if not row['caminho'] or not dest.is_file():
            errors.append('Fonte do Drive sem arquivo: ' + row['drive_id'])
        elif sha(dest.read_bytes()) != row['sha256']:
            errors.append('Cópia da cobertura do Drive alterada: ' + row['caminho'])
    if errors:
        for err in errors:
            print('ERRO: ' + err)
        raise SystemExit(1)
    print(f'OK: {len(files)} itens catalogados; {len(rows)} caminhos migrados; 45 fontes na matriz; 2.171 registros; 43 modelos.')
    print('OK: hashes, blocos copiáveis, células da matriz, links locais e nomes compatíveis com Windows.')
    print('A validação é local; não comprova eficácia comercial, atualidade de fontes externas ou cadastro no CRM.')


if __name__ == '__main__':
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8')
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('acao', choices=['atualizar', 'validar'])
    args = parser.parse_args()
    update() if args.acao == 'atualizar' else validate()
