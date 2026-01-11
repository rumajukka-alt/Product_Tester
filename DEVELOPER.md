# Developer checks

- `requirements-dev.txt`: contains developer tools (`black`, `isort`, `flake8`, `mypy`, `pre-commit`, `pytest`).
- Install dev dependencies:

```bash
python -m venv .venv
# On Linux/macOS
source .venv/bin/activate
# On Windows PowerShell
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
pip install -r requirements-dev.txt
```

- Install pre-commit hooks:

```bash
pre-commit install
pre-commit run --all-files
```

- Run checks locally:

```bash
black --check .
isort --check .
flake8
mypy .
pytest -q
```

These checks help prevent accidental regressions and import-time errors. Add or extend tests under `tests/`.

---

**Mypy / tyyppitarkistus**

- Huom: projektin pakettirakenne voi aiheuttaa, että `mypy`-pre-commit-hook ei toimi suoraan tässä repossa. Siksi `mypy`-hook on jätetty pois `.pre-commit-config.yaml`-tiedostosta.
- Aja `mypy` paikallisesti virtualenvissä näin:

```bash
# Aktivoi virtuaaliympäristö (PowerShell)
.\.venv\Scripts\Activate.ps1
# Suorita mypy vain projektin lähdepaketille
python -m mypy Code
```

- Jos haluat ottaa `mypy`-hookin takaisin käyttöön pre-commitissa, avaa `.pre-commit-config.yaml` ja kommentoi takaisin mypy-sektio sekä lisää tarvittavat `args` (esim. `--explicit-package-bases`) tai säädä `MYPYPATH` niin että mypy näkee projektin paketit yksikäsitteisesti.

