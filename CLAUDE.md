# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

**Contratos semánticos temporales** ("Temporal Semantic Contracts") — a Spanish-language, formative and practical kit for designing, documenting, validating and evaluating short, versioned semantic contracts that pin down how an LLM must interpret an assignment. The full conceptual rationale and authoritative spec live at [.docs/cts.md](.docs/cts.md); the rest of the tree is the realised implementation of that spec.

## Working language

Everything user-facing is **in Spanish**: docs, examples, READMEs, issue/PR templates, training material, commit messages for content changes. If a word like "profesional", "claro" or "neutral" carries weight in something you write, define it.

## Domain concept (needed to make sensible edits)

A **contrato semántico temporal** is the document type the project is *about*. It is short, task-scoped, versionable, and fixes for one specific LLM assignment:

1. operational meaning of ambiguous terms (`terminos`),
2. priority order when criteria conflict (`prioridades`),
3. what counts as an error (`errores`),
4. how uncertainty must be handled (`incertidumbre` — fact / inference / gap),
5. acceptance criteria for the output (`salida` — format, sections, max words, forbidden tokens).

Every example under [examples/](examples/) ships with a `README.md` (prompt + intended output) and a `test_case.json` (full contract + `expected_output` block consumed by the test runner). Sensitive domains — [examples/salud/](examples/salud/) and [examples/legal/](examples/legal/) — **must** mark `incertidumbre.escalar_a_humano: true` and require human review in their contracts. This is a hard rule from [CONTRIBUTING.md](CONTRIBUTING.md), not a suggestion.

The structural source of truth is [schemas/contrato.schema.json](schemas/contrato.schema.json) (JSON Schema 2020-12). Any contract — whether in `templates/`, `examples/*/test_case.json`, or new domains you add — must validate against it.

## Architecture (how the pieces fit together)

The validation loop has three independent layers that compound:

1. **Structural** — `schemas/contrato.schema.json` defines required fields and types. [scripts/validate_contracts.py](scripts/validate_contracts.py) walks `templates/` and `examples/`, extracts each contract (templates are contracts; `test_case.json` wraps a contract under the `contract` key) and validates it against the schema.
2. **Behavioural** — [scripts/simulate_model.py](scripts/simulate_model.py) is a deterministic stand-in for an LLM. It holds a hardcoded `DOMAIN_SECTIONS` dict keyed by domain (one entry per example folder); given a `test_case.json`, it emits sections in the order of `expected_output.priority_order`, truncating to `expected_output.max_words`. [scripts/run_example_tests.py](scripts/run_example_tests.py) feeds every `test_case.json` through this simulator and asserts: required tokens present, forbidden tokens absent, priority tokens appear in declared order, length cap respected.
3. **Pytest** — [tests/](tests/) re-asserts the structural layer (`test_contract_schema.py`), repeats domain-specific behavioural checks (`test_priority_rules.py`), and enforces the "at least 6 domains, each with README + test_case" invariant (`test_examples_presence.py`).

**Cross-cutting gotcha — token collision in the behavioural layer.** `run_example_tests.py` uses `str.find()` to locate priority tokens in order. If a priority token (e.g. `"riesgo"`) appears as a substring inside an *earlier* section's content, the order check fails. When you edit `DOMAIN_SECTIONS` in `simulate_model.py` or change `priority_order` in any `test_case.json`, scan each section's content for substrings that match *later* priority tokens. The `legal` example was caught by exactly this: an earlier draft had "riesgos interpretativos" in the Supuesto content, which collided with the later `riesgo` priority. It now reads "dudas interpretativas".

**Coupling between scripts and examples.** Adding a new domain folder under `examples/` requires three coordinated changes:
1. Add an entry to `DOMAIN_SECTIONS` in `scripts/simulate_model.py` with one key per section name in `expected_output.priority_order` (use the capitalised form — the simulator does `section_name.capitalize()` to look up the title).
2. Create `examples/<dominio>/README.md` and `examples/<dominio>/test_case.json` matching the schema.
3. If the example needs a domain-specific assertion beyond the generic loop, add a test to `tests/test_priority_rules.py`.

The `.github/workflows/` directory has three CI jobs — `validate-contract-presence.yml`, `lint-json-yaml.yml`, `run-example-tests.yml` — that mirror the three validation layers above. If you modify a script the workflows invoke, update both ends.

## Commands

Dev deps (Python 3.11+ per the CI workflows):

```bash
python -m pip install -U jsonschema pyyaml pytest yamllint
```

Validate every contract (templates + examples) against the schema:

```bash
python scripts/validate_contracts.py
```

Run the example-driven behavioural tests:

```bash
python scripts/run_example_tests.py
```

Full pytest suite (structural + behavioural + presence):

```bash
pytest -q
```

Single test file / single test:

```bash
pytest tests/test_contract_schema.py
pytest tests/test_priority_rules.py::test_orden_de_prioridades_en_corporativo
```

Lint YAML (CI uses `yamllint .`):

```bash
yamllint .
```

Build the training slide deck (requires Node + Marp CLI):

```bash
bash scripts/build_slides_pdf.sh
```

PR gate (only meaningful inside GitHub Actions with `GITHUB_EVENT_PATH` set):

```bash
python scripts/check_pr_semantic_contract.py
```

### Windows console encoding

The scripts print a UTF-8 check mark (`✔`). On Windows shells whose default code page is cp1252, set `PYTHONIOENCODING=utf-8` before running anything that prints to stdout, or stdout will raise `UnicodeEncodeError`:

```bash
PYTHONIOENCODING=utf-8 python scripts/run_example_tests.py
```

CI is unaffected (Linux runners default to UTF-8).

## Spec ↔ tree consistency rule

[.docs/cts.md](.docs/cts.md) is the authoritative blueprint — every materialised file in this tree was extracted from a fenced code block under a `#### \`path/to/file\`` heading in that document. The rule is bidirectional:

- **When you edit a materialised file**, if the change is anything more than a typo, also update the corresponding fenced block in `.docs/cts.md` so the spec doesn't drift.
- **When the spec changes**, re-materialise the affected files.

To locate the canonical block for any path, grep the spec for the path string:

```
Grep -n "scripts/simulate_model.py" .docs/cts.md
Grep -n "examples/salud/test_case.json" .docs/cts.md
```

## Conventions worth preserving

- Folder names: lowercase, hyphen-separated.
- Domain names in `examples/` must match the keys in `DOMAIN_SECTIONS` exactly (lowercase, hyphenated — e.g. `ux-producto`, `investigacion-academica`).
- Don't accept examples that normalise fabrication or filler content (per `CONTRIBUTING.md`).
- Bibliography additions: prefer primary sources, Spanish-language texts, and official documentation, in that order.
- Licence is MIT.
