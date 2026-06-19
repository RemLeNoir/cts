from __future__ import annotations

import json
from pathlib import Path

from simulate_model import generate_output

ROOT = Path(__file__).resolve().parents[1]
EXAMPLES = ROOT / "examples"

def check_test_case(path: Path) -> None:
    data = json.loads(path.read_text(encoding="utf-8"))
    output = generate_output(data)
    lower_output = output.lower()
    expected = data["expected_output"]

    for token in expected.get("must_include", []):
        assert token.lower() in lower_output, f"Falta token requerido '{token}' en {path}"

    for token in expected.get("must_not_include", []):
        assert token.lower() not in lower_output, f"Token prohibido '{token}' en {path}"

    order = expected.get("priority_order", [])
    last_index = -1
    for token in order:
        idx = lower_output.find(token.lower())
        assert idx != -1, f"No aparece la prioridad '{token}' en {path}"
        assert idx > last_index, f"Orden incorrecto para '{token}' en {path}"
        last_index = idx

    max_words = expected.get("max_words")
    if max_words:
        assert len(output.split()) <= max_words, f"Se supera max_words en {path}"

def main() -> None:
    files = sorted(EXAMPLES.rglob("test_case.json"))
    assert files, "No se encontraron casos de prueba."

    for path in files:
        check_test_case(path)
        print(f"✔ OK: {path.relative_to(ROOT)}")

    print(f"Ejemplos verificados: {len(files)}")

if __name__ == "__main__":
    main()
