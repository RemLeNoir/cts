"""Parsea biblioteca/biblioteca.md y produce biblioteca/biblioteca.json.

Estructura de entrada esperada:

    # Biblioteca de contratos semánticos para IA

    Subtítulo o intro opcional.

    ---

    ## N. Título de la sección

    Párrafo de intro opcional (no es la fila de cabecera ni separador).

    | Columna A | Columna B |
    |---|---|
    | celda A1 | celda B1 |
    ...

    ---

    ## Regla transversal

    Párrafo final sin tabla.

Cada sección con número se parsea como una `seccion`. La regla transversal
se guarda aparte. La sección `Regla transversal` (sin número) se reconoce
por el título.

La fuente canónica es markdown porque facilita edición humana, revisión
visual en GitHub y diff en PRs. El JSON producido sirve al frontend
estático `index.html`, que no tiene runtime.
"""

from __future__ import annotations

import json
import re
import sys
import unicodedata
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "biblioteca" / "biblioteca.md"
TARGET = ROOT / "biblioteca" / "biblioteca.json"

SECTION_RE = re.compile(r"^##\s+(?:(\d+)\.\s+)?(.+?)\s*$")
SEPARATOR_RE = re.compile(r"^---\s*$")
TABLE_ROW_RE = re.compile(r"^\|(.*)\|\s*$")
TABLE_SEP_ROW_RE = re.compile(r"^\|\s*:?-+:?\s*(\|\s*:?-+:?\s*)+\|\s*$")


def slugify(text: str) -> str:
    """Convierte un título a slug ASCII estable.

    `Aduanas, fiscalidad y contexto Canarias` -> `aduanas-fiscalidad-y-contexto-canarias`.
    """

    text = unicodedata.normalize("NFKD", text)
    text = text.encode("ascii", "ignore").decode("ascii")
    text = text.lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-")


def parse_table_row(line: str) -> list[str]:
    inner = TABLE_ROW_RE.match(line).group(1)
    cells = [c.strip() for c in inner.split("|")]
    return cells


def is_table_separator(line: str) -> bool:
    return bool(TABLE_SEP_ROW_RE.match(line))


def split_sections(lines: list[str]) -> list[dict]:
    """Recorre las líneas y agrupa contenido por sección.

    Devuelve una lista de dicts con campos `numero` (str|None), `titulo`,
    `cuerpo` (lista de líneas brutas), preservando el orden de aparición.
    """

    sections: list[dict] = []
    current: dict | None = None
    in_preamble = True

    for line in lines:
        m = SECTION_RE.match(line)
        if m:
            if current is not None:
                sections.append(current)
            current = {
                "numero": m.group(1),
                "titulo": m.group(2).strip(),
                "cuerpo": [],
            }
            in_preamble = False
            continue
        if in_preamble:
            # Saltamos cabecera del documento (título h1, blanco, intro).
            continue
        if current is not None and not SEPARATOR_RE.match(line):
            current["cuerpo"].append(line)
    if current is not None:
        sections.append(current)
    return sections


def parse_section(section: dict) -> dict:
    """Convierte una sección bruta en su forma estructurada.

    Detecta encabezados de tabla, filas, intro opcional y especialidad
    de tipo (`meta` para sección 0, `antipatrones` para la que tenga
    cabecera "Por qué no tiene versión válida"; el resto es
    `transformaciones`).
    """

    body = section["cuerpo"]
    # Localizar la primera línea que parezca cabecera de tabla.
    header_idx = None
    for i, line in enumerate(body):
        stripped = line.strip()
        if not stripped:
            continue
        if TABLE_ROW_RE.match(stripped) and not is_table_separator(stripped):
            header_idx = i
            break
    intro_lines: list[str] = []
    headers: list[str] = []
    rows: list[list[str]] = []

    if header_idx is None:
        # Sección sin tabla: todo es cuerpo prosa (regla transversal).
        prose = "\n".join(line.strip() for line in body if line.strip()).strip()
        return {
            "numero": section["numero"],
            "titulo": section["titulo"],
            "id": slugify(
                f"{section['numero']}-{section['titulo']}"
                if section["numero"]
                else section["titulo"]
            ),
            "tipo": "regla",
            "intro": None,
            "encabezados": [],
            "filas": [],
            "texto": prose,
        }

    # Intro = todo lo no vacío antes de la cabecera.
    for line in body[:header_idx]:
        if line.strip():
            intro_lines.append(line.strip())
    intro = " ".join(intro_lines) if intro_lines else None

    # La cabecera.
    headers = parse_table_row(body[header_idx].strip())

    # Línea de separador justo después.
    after_header = header_idx + 1
    while after_header < len(body) and not body[after_header].strip():
        after_header += 1
    if after_header < len(body) and is_table_separator(body[after_header].strip()):
        after_header += 1

    # El resto: filas de tabla.
    for line in body[after_header:]:
        stripped = line.strip()
        if not stripped:
            continue
        m = TABLE_ROW_RE.match(stripped)
        if not m:
            # Permitimos que tras la tabla pueda haber prosa adicional;
            # paramos al primer no-fila.
            break
        if is_table_separator(stripped):
            continue
        cells = parse_table_row(stripped)
        # Acepta filas con exactamente el ancho declarado.
        if len(cells) == len(headers):
            rows.append(cells)

    # Tipo de sección.
    if section["numero"] == "0":
        tipo = "meta"
    elif (
        len(headers) >= 2
        and "no tiene versi" in headers[1].lower()
    ):
        tipo = "antipatrones"
    else:
        tipo = "transformaciones"

    seccion_id = slugify(
        f"{section['numero']}-{section['titulo']}"
        if section["numero"]
        else section["titulo"]
    )

    return {
        "numero": section["numero"],
        "titulo": section["titulo"],
        "id": seccion_id,
        "tipo": tipo,
        "intro": intro,
        "encabezados": headers,
        "filas": rows,
    }


def build() -> dict:
    text = SOURCE.read_text(encoding="utf-8")
    lines = text.splitlines()

    raw_sections = split_sections(lines)
    parsed = [parse_section(s) for s in raw_sections]

    # Separar la regla transversal en su propio campo.
    secciones = [p for p in parsed if p["tipo"] != "regla"]
    regla = next((p for p in parsed if p["tipo"] == "regla"), None)

    total_filas = sum(len(s["filas"]) for s in secciones)

    return {
        "version": "1",
        "generado": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "fuente": str(SOURCE.relative_to(ROOT)).replace("\\", "/"),
        "estadisticas": {
            "secciones": len(secciones),
            "filas": total_filas,
        },
        "secciones": secciones,
        "regla_transversal": regla["texto"] if regla else None,
    }


def main() -> int:
    if not SOURCE.exists():
        print(f"ERROR: no existe {SOURCE.relative_to(ROOT)}", file=sys.stderr)
        return 1
    data = build()
    serialized = json.dumps(data, ensure_ascii=False, indent=2)
    TARGET.write_text(serialized + "\n", encoding="utf-8")
    print(
        f"OK: {data['estadisticas']['secciones']} secciones, "
        f"{data['estadisticas']['filas']} filas. "
        f"-> {TARGET.relative_to(ROOT)}"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
