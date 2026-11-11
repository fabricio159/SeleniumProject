# SeleiumProject

Selenium + pytest test automation for https://www.saucedemo.com/.

## Project layout

```
SeleiumProject/
├── config/          # Config class (reads .env)
├── pages/           # page objects (BasePage, LoginPage, InventoryPage)
├── utils/           # driver_factory and other helpers
├── tests/
│   ├── test_smoke.py    # plain pytest tests
│   ├── features/        # BDD scenarios in Gherkin (.feature)
│   └── step_defs/       # step definitions for the scenarios (pytest-bdd)
├── conftest.py      # driver fixture, --browser / --headless options
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
HEADLESS=false
PAGE_LOAD_TIMEOUT=30
EXPLICIT_WAIT=5
```

Timeouts are in seconds.

To reproduce the exact versions used by the team or CI instead:

```bash
pip install -r requirements.txt
pip install -e . --no-deps
```

## Running tests

Always work from the project root with the venv activated:

```bash
cd ~/SeleiumProject
source .venv/bin/activate
```

Every run writes `report.html` in the project root. Open it in a browser to see the results.

### All tests

```bash
pytest                            # everything: smoke + BDD
pytest -v                         # list each test with its result
```

### Browser options

These options work with every command below:

```bash
pytest --headless                 # no browser window (CI, faster)
pytest --browser chrome           # override BROWSER from .env
```

### Plain pytest tests

```bash
pytest tests/test_smoke.py        # run one file
pytest -k open_page               # run tests whose name matches
```

### BDD (Gherkin) tests

```bash
pytest tests/step_defs                     # all scenarios
pytest tests/step_defs -v                  # list scenarios by name
pytest tests/step_defs/test_login.py       # one feature
pytest tests/step_defs -k "successful"     # scenarios whose name matches
pytest tests/step_defs -m smoke            # scenarios tagged @smoke
pytest tests/step_defs -m "not smoke"      # everything except @smoke
```

Before using a tag such as `@smoke`, register it under `markers` in `[tool.pytest.ini_options]` in `pyproject.toml`. Otherwise pytest warns about an unknown marker.

### Debugging a failure

```bash
pytest -x                         # stop at the first failure
pytest --lf                       # re-run only the tests that failed last time
pytest -s                         # show print() output
```

### Running a module directly

```bash
python -m utils.driver_factory
```

## Adding a BDD feature

1. Write the scenarios in `tests/features/<name>.feature`.
2. Create `tests/step_defs/test_<name>.py`, starting with `scenarios("../features/<name>.feature")`.
3. Run `pytest tests/step_defs`. Any step without a definition fails with an error naming the missing step.

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
| Edited code in `config/`, `pages/`, `utils/`, or `tests/` | Nothing, editable install picks it up |
| Added a new top-level package folder | Add it to `packages` in `pyproject.toml`, then `pip install -e ".[dev]"` |
| Running all tests | `pytest` |
| Running only BDD scenarios | `pytest tests/step_defs` |
| Running in CI or without a window | `pytest --headless` |
