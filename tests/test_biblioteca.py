"""Tests del build de la biblioteca y de la coherencia entre fuente y JSON."""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from build_biblioteca import build  # noqa: E402


def test_fuente_y_json_existen():
    assert (ROOT / "biblioteca" / "biblioteca.md").is_file()
    assert (ROOT / "biblioteca" / "biblioteca.json").is_file()


def test_build_produce_contenido_no_trivial():
    data = build()
    assert data["estadisticas"]["secciones"] >= 1
    assert data["estadisticas"]["filas"] >= 1
    assert data["regla_transversal"], "Falta la regla transversal."


def test_estructura_de_cada_seccion():
    data = build()
    ids = set()
    for s in data["secciones"]:
        assert s["id"], "Sección sin id"
        assert s["id"] not in ids, f"ID duplicado: {s['id']}"
        ids.add(s["id"])
        assert s["titulo"], "Sección sin título"
        assert s["tipo"] in {"meta", "transformaciones", "antipatrones"}, (
            f"Tipo desconocido en {s['titulo']}: {s['tipo']}"
        )
        assert len(s["encabezados"]) == 2, (
            f"Se esperan exactamente 2 columnas en {s['titulo']}"
        )
        for row in s["filas"]:
            assert len(row) == 2, (
                f"Fila con columnas != 2 en {s['titulo']}: {row}"
            )
            assert row[0], f"Celda A vacía en {s['titulo']}"
            assert row[1], f"Celda B vacía en {s['titulo']}"


def test_json_commiteado_coincide_con_fuente():
    """Si alguien modifica biblioteca.md sin regenerar el JSON, este test falla.

    El campo `generado` se ignora porque es un timestamp.
    """
    fresh = build()
    committed = json.loads(
        (ROOT / "biblioteca" / "biblioteca.json").read_text(encoding="utf-8")
    )
    fresh.pop("generado", None)
    committed.pop("generado", None)
    assert fresh == committed, (
        "El JSON commiteado no coincide con biblioteca/biblioteca.md. "
        "Ejecuta `python scripts/build_biblioteca.py` y commitea el cambio."
    )


def test_seccion_cero_es_meta():
    data = build()
    cero = next((s for s in data["secciones"] if s["numero"] == "0"), None)
    assert cero is not None, "Falta la sección 0 con las cláusulas meta."
    assert cero["tipo"] == "meta"


def test_existe_antipatrones():
    data = build()
    anti = [s for s in data["secciones"] if s["tipo"] == "antipatrones"]
    assert anti, "Falta la sección de antipatrones."
    for s in anti:
        assert "no tiene versi" in s["encabezados"][1].lower(), (
            "La sección de antipatrones debe tener segunda columna 'Por qué no tiene versión válida'."
        )
