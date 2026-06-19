import json
from pathlib import Path

from jsonschema import validate
import yaml

ROOT = Path(__file__).resolve().parents[1]
SCHEMA = json.loads((ROOT / "schemas" / "contrato.schema.json").read_text(encoding="utf-8"))

def test_template_json_valida():
    data = json.loads((ROOT / "templates" / "contrato-semantico.json").read_text(encoding="utf-8"))
    validate(instance=data, schema=SCHEMA)

def test_template_yaml_valida():
    data = yaml.safe_load((ROOT / "templates" / "contrato-semantico.yaml").read_text(encoding="utf-8"))
    validate(instance=data, schema=SCHEMA)

def test_todos_los_test_case_tienen_contrato_valido():
    for path in (ROOT / "examples").rglob("test_case.json"):
        data = json.loads(path.read_text(encoding="utf-8"))
        validate(instance=data["contract"], schema=SCHEMA)
