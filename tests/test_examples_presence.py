from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def test_hay_seis_dominios_minimos():
    domains = [p for p in (ROOT / "examples").iterdir() if p.is_dir()]
    assert len(domains) >= 6

def test_cada_dominio_tiene_readme_y_test_case():
    for domain in (ROOT / "examples").iterdir():
        if not domain.is_dir():
            continue
        assert (domain / "README.md").exists()
        assert (domain / "test_case.json").exists()
