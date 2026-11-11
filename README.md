# SeleiumProject

Selenium + pytest test automation for https://www.saucedemo.com/.

## Project layout

```
SeleiumProject/
├── config/          # Config class (reads .env)
├── utils/           # driver_factory and other helpers
├── tests/           # pytest tests
├── .env             # BROWSER, BASE_URL (not committed)
├── pyproject.toml   # project definition, dependencies, pytest settings
└── requirements.txt # exact pinned versions (lock file)
```

## Setup (first time / new machine / new venv)

```bash
cd ~/SeleiumProject
python3 -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
```

Create a `.env` file in the project root:

```
BROWSER=chrome
BASE_URL=https://www.saucedemo.com/
```

To reproduce the exact versions used by the team or CI instead:

```bash
pip install -r requirements.txt
pip install -e . --no-deps
```

## Daily workflow

Always work from the project root with the venv activated:

```bash
cd ~/SeleiumProject
source .venv/bin/activate

pytest                            # run all tests, writes report.html
pytest tests/test_smoke.py        # run one file
pytest -k open_page               # run tests matching a name

python -m utils.driver_factory    # run a module directly
```

## Adding or upgrading a dependency

1. Add it to `pyproject.toml`: to `dependencies` if the code needs it to run, or to `dev` if it is only needed for testing.
2. Reinstall and refresh the lock file:

```bash
pip install -e ".[dev]"
pip freeze --exclude-editable > requirements.txt
```

3. Commit both `pyproject.toml` and `requirements.txt`.

## When to run what

| Situation | Command |
|---|---|
| First clone, new machine, or deleted/recreated `.venv` | `pip install -e ".[dev]"` |
| Pulled changes that modified `pyproject.toml` | `pip install -e ".[dev]"` |
| Need the exact versions CI uses | `pip install -r requirements.txt` then `pip install -e . --no-deps` |
| Added, removed, or upgraded a dependency | `pip install -e ".[dev]"` then `pip freeze --exclude-editable > requirements.txt` |
| Edited code in `config/`, `utils/`, or `tests/` | Nothing, editable install picks it up |
| Added a new top-level package folder | Add it to `packages` in `pyproject.toml`, then `pip install -e ".[dev]"` |
| Running tests | `pytest` |
