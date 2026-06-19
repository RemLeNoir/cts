from __future__ import annotations

import json
from pathlib import Path

import yaml
from jsonschema import validate

ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = ROOT / "schemas" / "contrato.schema.json"

def load_schema() -> dict:
    return json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))

def load_data(path: Path) -> dict:
    if path.suffix == ".json":
      return json.loads(path.read_text(encoding="utf-8"))
    if path.suffix in {".yml", ".yaml"}:
      return yaml.safe_load(path.read_text(encoding="utf-8"))
    raise ValueError(f"Formato no soportado: {path}")

def iter_contract_files() -> list[Path]:
    candidates = []
    for directory in [ROOT / "templates", ROOT / "examples"]:
        for path in directory.rglob("*"):
            if path.suffix in {".json", ".yml", ".yaml"}:
                candidates.append(path)
    return candidates

def extract_contract(data: dict, path: Path) -> dict | None:
    # Los test_case.json guardan el contrato bajo la clave "contract".
    if path.name == "test_case.json":
        return data.get("contract")
    # Las plantillas JSON/YAML son contratos directos.
    if path.name.startswith("contrato-semantico"):
        return data
    return None

def main() -> None:
    schema = load_schema()
    checked = 0

    for path in iter_contract_files():
        data = load_data(path)
        contract = extract_contract(data, path)

        if contract is None:
            continue

        validate(instance=contract, schema=schema)
        checked += 1
        print(f"✔ Validado: {path.relative_to(ROOT)}")

    if checked == 0:
        raise SystemExit("No se ha encontrado ningún contrato para validar.")

    print(f"Validación completada. Contratos validados: {checked}")

if __name__ == "__main__":
    main()
