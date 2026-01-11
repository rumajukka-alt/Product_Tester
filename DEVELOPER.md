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
