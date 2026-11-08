# Groundwater Drawdown Simulator — Suggested Project Structure

## 1. Design philosophy

This is a **small scientific Python project**, not a production web service. Keep the initial architecture simple enough that you can write and understand each module yourself. Use Spyder for interactive runs, plots, and variable inspection, while separating reusable scientific functions from experiment scripts.

Use `uv` for dependencies and a project-local `.venv`. Keep generated plots and local environments out of Git. Add complexity only when a specific scientific need emerges.

## 2. Recommended directory tree

```text
groundwater_drawdown/
├── README.md
├── PROJECT_OVERVIEW.md
├── PROJECT_STRUCTURE.md
├── development_log.md
├── pyproject.toml
├── uv.lock
├── .python-version
├── .gitignore
├── .gitattributes
│
├── data/
│   ├── raw/
│   ├── synthetic/
│   └── processed/
│
├── docs/
│   ├── 00_overview/
│   │   └── 00_project_overview.md
│   │
│   ├── 01_architecture/
│   │   └── 00_project_structure.md
│   │
│   ├── 02_engineering_documentation/
│   │   ├── 00_groundwater_initial_test_scenario.md
│   │   ├── 01_engineering_background_outline.md
│   │   ├── 02_engineering_background_foundation.md
│   │   ├── 03_mathematical_background.md
│   │   ├── 04_model_assumptions.md
│   │   ├── 05_validation_plan.md
│   │   └── 06_development_log.md
│   │
│   └── 03_checklists/
│       └── 00_checklist.md
│   
├── src/
│   └── groundwater_drawdown/
│       ├── __init__.py
│       │
│       ├── models/
│       │   ├── __init__.py
│       │   └── theis.py
│       │
│       ├── numerical/
│       │   └── __init__.py
│       │
│       ├── calibration/
│       │   └── __init__.py
│       │
│       ├── uncertainty/
│       │   └── __init__.py
│       │
│       ├── analysis/
│       │   └── __init__.py
│       │
│       ├── visualization/
│       │   └── __init__.py
│       │
│       └── utils/
│           └── __init__.py
│
├── experiments/
│   ├── 01_deterministic/
│   ├── 02_sensitivity/
│   ├── 03_calibration/
│   ├── 04_monte_carlo/
│   └── 05_bayesian/
│
├── tests/
│   ├── test_models/
│   ├── test_numerical/
│   ├── test_calibration/
│   └── test_uncertainty/
│
└── results/
    ├── figures/
    ├── tables/
    └── reports/
```

**Not shown in Git:** `.venv/`, `.spyproject/` (if created), `__pycache__/`, `.pytest_cache/`, and other temporary files.

The `results/` directory is for generated outputs. Keep directory placeholders if needed, but do not automatically commit every generated result.

## 3. Purpose of each file and directory

| Path | Responsibility |
|---|---|
| `README.md` | Repository introduction, installation instructions, running experiments, project status, and example outputs |
| `pyproject.toml` | Python project metadata, dependencies, and development tool configuration |
| `uv.lock` | Locked dependency versions for reproducible environments |
| `.python-version` | Pinned Python version used by uv |
| `.gitignore` | Excludes virtual environments, caches, Spyder metadata, and generated files |
| `.gitattributes` | Consistent Git line-ending behavior across Windows and Linux |
| `docs/00_project_overview.md` | Engineering problem statement, project objectives, scope, and acceptance criteria |
| `docs/01_mathematical_background.md` | Theis equations, groundwater flow theory, parameter definitions, and units |
| `docs/02_model_assumptions.md` | Hydrogeologic assumptions, model limitations, and applicability |
| `docs/03_validation_plan.md` | Analytical benchmarks, physical behavior checks, numerical tolerances, and validation criteria |
| `docs/development_log.md` | Date-stamped implementation notes, debugging observations, lessons learned, and decisions |
| `data/raw/` | Original observed groundwater measurements or external reference datasets |
| `data/synthetic/` | Generated pumping-test datasets with known model parameters |
| `data/processed/` | Cleaned and transformed datasets used for calibration or analysis |
| `src/groundwater_drawdown/__init__.py` | Defines the groundwater_drawdown Python package |
| `src/groundwater_drawdown/models/` | Physical groundwater models and analytical solutions |
| `src/groundwater_drawdown/models/theis.py` | Theis well function, dimensionless parameter, and transient drawdown calculations |
| `src/groundwater_drawdown/numerical/` | Shared numerical algorithms and solvers when required by future models |
| `src/groundwater_drawdown/calibration/` | Parameter estimation, optimization, fitting observed drawdown data, and calibration diagnostics |
| `src/groundwater_drawdown/uncertainty/` | Probability distributions, Monte Carlo simulation, Bayesian inference, and uncertainty propagation |
| `src/groundwater_drawdown/analysis/` | Sensitivity analysis, scenario comparisons, and interpretation of groundwater model results |
| `src/groundwater_drawdown/visualization/` | Reusable plotting functions for drawdown curves, parameter comparisons, and uncertainty results |
| `src/groundwater_drawdown/utils/` | Shared input validation, unit conversions, and general-purpose utilities |
| `experiments/01_deterministic/` | Single-point drawdown calculations, time-drawdown curves, and radial drawdown profiles |
| `experiments/02_sensitivity/` | Controlled experiments varying transmissivity, storativity, pumping rate, and distance |
| `experiments/03_calibration/` | Parameter estimation experiments using synthetic or observed pumping-test data |
| `experiments/04_monte_carlo/` | Stochastic simulations evaluating uncertainty in groundwater drawdown predictions |
| `experiments/05_bayesian/` | Bayesian parameter estimation, posterior analysis, and predictive uncertainty experiments |
| `tests/test_models/` | Automated tests for physical equations, expected drawdown behavior, and input validation |
| `tests/test_numerical/` | Numerical accuracy, convergence, and solver verification tests |
| `tests/test_calibration/` | Parameter recovery tests, fitting accuracy, and calibration behavior |
| `tests/test_uncertainty/` | Statistical sampling, reproducibility, and uncertainty propagation tests |
| `results/figures/` | Exported hydrogeologic plots, sensitivity figures, and probability distributions |
| `results/tables/` | CSV files containing simulation outputs, parameter estimates, and statistical summaries |
| `results/reports/` | Scientific interpretation, validation summaries, and experiment reports |

## 4. Module boundaries

### `theis.py`

Write small functions with explicit inputs and outputs. Suggested responsibilities:

- Compute the dimensionless Theis parameter \(u\).
- Evaluate the well function using `scipy.special.exp1`.
- Calculate drawdown from \(Q,T,S,r,t\).
- Support NumPy arrays for time or radius without hiding the governing equation.

Do **not** include plotting, file writes, or interactive prompts in this module.

### `validation.py`

Centralize checks for required positive parameters, nonnegative pumping rate, finite numeric values, and compatible array inputs. Begin with straightforward checks. A complex validation framework is unnecessary.

### `experiments/`

Each script should have one purpose: set input values, call reusable model functions, inspect results, and create a figure or table. These scripts are the primary files you will run interactively in Spyder.

### `tests/`

Test the physics and code behavior, not the appearance of the plots. Examples: zero pumping, pumping-rate scaling, monotonic trends, scalar/array agreement, and invalid input handling.

## 5. Dependencies

Start with:

| Package | Purpose | When needed |
|---|---|---|
| `numpy` | Numeric arrays and vectorized calculations | Phase 1–2 |
| `scipy` | Theis well function (`scipy.special.exp1`) | Phase 1 |
| `matplotlib` | Scientific plotting | Phase 2 |
| `pytest` | Automated tests | Phase 1 onward |
| `spyder-kernels` | Connect a project interpreter to Spyder | If using the project `.venv` as Spyder's interpreter |

`pandas` is optional until you need convenient CSV/table workflows. You do not need a Bayesian library or Monte Carlo framework for the deterministic model.

## 6. Windows + uv setup

In Git Bash or PowerShell, from the directory where you keep repositories:

```bash
uv init --package groundwater_drawdown
cd groundwater_drawdown
uv python pin 3.12
uv add numpy scipy matplotlib
uv add --dev pytest
```

`uv init --package` creates a packaged `src/` layout. You can then add the scientific modules and experiment scripts shown above. If the repository already exists, **do not reinitialize it**; adapt its current `pyproject.toml` and structure instead.

To use the `.venv` interpreter inside Spyder, install a **Spyder-compatible** `spyder-kernels` version into the project environment:

```bash
uv add --dev spyder-kernels
```

Then point **Tools → Preferences → Python Interpreter** to:

```text
<project-path>\.venv\Scripts\python.exe
```

Restart the IPython console. If Spyder reports a kernel version mismatch, check Spyder's stated required `spyder-kernels` range and pin a compatible version rather than changing the entire environment.

**Important:** The standalone Spyder application and the project's `.venv` are separate installations. Do not install the full Spyder IDE into every project.

## 7. Suggested `.gitignore`

```gitignore
# Python environments
.venv/
venv/

# Python caches and tests
__pycache__/
*.py[cod]
.pytest_cache/
.coverage

# Spyder local project settings
.spyproject/

# Generated scientific outputs
results/figures/*
results/tables/*
!results/figures/.gitkeep
!results/tables/.gitkeep

# Operating system / editor clutter
.DS_Store
Thumbs.db
```

Keep `pyproject.toml`, `uv.lock`, and `.python-version` tracked.

## 8. Suggested `.gitattributes`

```gitattributes
* text=auto
*.py text eol=lf
*.md text eol=lf
*.toml text eol=lf
*.yml text eol=lf
*.yaml text eol=lf
*.csv text eol=lf
*.bat text eol=crlf
*.png binary
*.jpg binary
*.pdf binary
```

This keeps source text consistent when moving between Windows and Linux.

## 9. Development sequence

| Milestone | Files to work on | Evidence of completion |
|---|---|---|
| 1. First calculation | `theis.py`, `01_single_point.py` | Correct, labeled drawdown for one case |
| 2. Input checking | `validation.py`, tests | Invalid physical inputs are rejected |
| 3. Time response | `02_time_drawdown.py` | Drawdown-versus-time plot |
| 4. Radial response | `03_radial_profile.py` | Drawdown-versus-radius plot |
| 5. Sensitivity | `04_parameter_sensitivity.py` | Controlled comparison plots and written interpretation |
| 6. Verification and documentation | `tests/`, `README.md`, `development_log.md` | Repeatable tests and clear assumptions |
| 7. Optional uncertainty | New `monte_carlo.py` and experiment | Reproducible drawdown distribution with justified inputs |

Do not create a `monte_carlo.py` module until you reach the optional extension. Resist adding classes, configuration frameworks, and abstractions merely to make the repository look sophisticated.

## 10. How to use Spyder for independent development

1. Open the project folder in Spyder and display Project Explorer.
2. Work on one experiment script at a time.
3. Implement the scientific function yourself before asking for code.
4. Use Spyder's Variable Explorer to inspect intermediate values such as \(u\), \(W(u)\), and drawdown arrays.
5. Use the debugger and small numerical examples when results look suspicious.
6. Save plots only after checking axes, units, and physical interpretation.
7. Run `uv run pytest` from the project directory as you add tests.
8. Record what you learned in `development_log.md`.

## 11. Definition of a successful structure

The repository is appropriately organized when you can:

- Run a single experiment in Spyder without executing unrelated scripts.
- Reuse the Theis calculations across multiple experiments.
- Explain why each file exists.
- Test numerical behavior without opening a plot window.
- Recreate the project environment using `uv sync`.
- Keep local settings and generated files from cluttering Git.

**Guiding rule:** The scientific model should drive the code structure, not the other way around.
