import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from simulate_model import generate_output  # noqa: E402

def test_orden_de_prioridades_en_corporativo():
    path = ROOT / "examples" / "corporativo" / "test_case.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    output = generate_output(data).lower()

    assert output.index("decisión") < output.index("beneficio") < output.index("riesgo") < output.index("siguiente paso")

def test_no_usa_terminos_prohibidos():
    path = ROOT / "examples" / "ux-producto" / "test_case.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    output = generate_output(data).lower()
    for token in data["expected_output"]["must_not_include"]:
        assert token.lower() not in output
