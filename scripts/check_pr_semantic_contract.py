from __future__ import annotations

import json
import os
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def get_event() -> dict:
    event_path = os.environ.get("GITHUB_EVENT_PATH")
    if not event_path:
        return {}
    return json.loads(Path(event_path).read_text(encoding="utf-8"))

def get_changed_files(base_sha: str, head_sha: str) -> list[str]:
    cmd = ["git", "diff", "--name-only", base_sha, head_sha]
    result = subprocess.run(cmd, capture_output=True, text=True, check=True)
    return [line.strip() for line in result.stdout.splitlines() if line.strip()]

def main() -> None:
    event = get_event()
    pr = event.get("pull_request", {})
    body = (pr.get("body") or "").lower()
    base_sha = pr.get("base", {}).get("sha")
    head_sha = pr.get("head", {}).get("sha")

    if not base_sha or not head_sha:
        print("Evento sin información de PR. No se aplica validación estricta.")
        return

    changed_files = get_changed_files(base_sha, head_sha)

    touches_semantic_content = any(
        path.startswith(("examples/", "templates/", "docs/")) for path in changed_files
    )
    has_contract_artifact = any(
        ("contrato" in path.lower()) or path.endswith("test_case.json")
        for path in changed_files
    )

    required_checkbox = "- [x] he añadido o actualizado un contrato semántico temporal cuando era necesario"

    if touches_semantic_content and not has_contract_artifact:
        raise SystemExit(
            "La PR modifica contenido semántico sin añadir ni actualizar un contrato o test_case.json."
        )

    if required_checkbox not in body:
        raise SystemExit(
            "La PR no marca la comprobación de contrato semántico en la plantilla."
        )

    print("✔ Presencia de contrato validada en la PR.")

if __name__ == "__main__":
    main()
