# Groundwater Drawdown Simulator

**Scientific Python | Groundwater Hydraulics | Numerical Modeling**

![Project Status](https://img.shields.io/badge/status-in%20development-yellow)
![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python&logoColor=white)
![IDE](https://img.shields.io/badge/IDE-Spyder-red)
![Package Manager](https://img.shields.io/badge/package%20manager-uv-purple)
![Scientific Computing](https://img.shields.io/badge/focus-scientific%20computing-teal)

> **Status:** In development. This repository is a learning-focused scientific computing project, built primarily in Spyder. Features described below are planned unless explicitly marked complete.

## Project overview

Groundwater pumping lowers hydraulic head in the surrounding aquifer. The resulting drawdown changes over time and varies with distance from the pumping well. This project investigates that behavior using the **Theis analytical solution** for transient radial flow toward a pumping well in an ideal confined aquifer.

The initial objective is to write and validate a deterministic Python model. Later phases will explore parameter sensitivity, uncertainty propagation, and comparison with observed or synthetic pumping-test data.

This is a standalone scientific computing project, **not** a web application or a groundwater design tool.

## Problem statement

For a confined aquifer pumped at a constant rate, how does groundwater drawdown vary with:

- Elapsed pumping time, $t$?
- Radial distance from the pumping well, $r$?
- Aquifer transmissivity, $T$?
- Aquifer storativity, $S$?
- Pumping rate, $Q$?

The project will calculate drawdown under specified assumptions, visualize the results, and check that the model behaves consistently with the governing equation.

## Scientific foundation

The Theis solution expresses drawdown as:

$$
s(r,t) = \frac{Q}{4\pi T} W(u)
$$

where

$$
u = \frac{r^2 S}{4Tt}
$$

and the well function is

$$
W(u) = E_1(u) = \int_u^\infty \frac{e^{-x}}{x}\,dx.
$$

| Symbol | Meaning | Example consistent SI units |
|---|---|---|
| $s$ | Drawdown | m |
| $Q$ | Constant pumping rate | m³/day |
| $T$ | Transmissivity | m²/day |
| $S$ | Dimensionless storativity | dimensionless |
| $r$ | Radial distance from pumping well | m |
| $t$ | Time since pumping began | days |
| $W(u)$ | Theis well function | dimensionless |

**Unit consistency is essential:** for the example units above, use days for time, meters for distance, and m³/day for pumping rate. SciPy provides the exponential integral through `scipy.special.exp1`.

### Modeling assumptions

The initial model assumes:

- A confined aquifer of effectively infinite areal extent.
- Homogeneous, isotropic aquifer properties with constant transmissivity and storativity.
- A fully penetrating pumping well with constant discharge.
- Horizontal radial flow governed by the idealized Theis formulation.
- Negligible wellbore storage, well losses, recharge, leakage, and boundary effects.
- Drawdown evaluated at positive radial distances and positive elapsed times.

These assumptions limit applicability to real groundwater systems. The model is intended for education and exploration, not engineering design without additional site-specific analysis.

## Development roadmap

### Phase 1: Single-point deterministic calculation

- [ ] Define inputs and their units.
- [ ] Implement a function that calculates $u$, $W(u)$, and drawdown.
- [ ] Validate input domains, including $T>0$, $S>0$, $r>0$, $t>0$, and an appropriate nonnegative pumping rate.
- [ ] Calculate drawdown at one observation point.
- [ ] Compare the result with an independent reference calculation.

**Milestone:** A reproducible, verified single-point calculation.

### Phase 2: Drawdown over time and distance

- [ ] Evaluate drawdown over a sequence of pumping times.
- [ ] Evaluate drawdown at multiple radial distances.
- [ ] Plot drawdown versus time and distance using Matplotlib.
- [ ] Label axes and document units.
- [ ] Investigate expected trends and limiting behavior.

**Milestone:** Interpretable drawdown curves and a radial drawdown profile.

### Phase 3: Parameter sensitivity

- [ ] Vary pumping rate, transmissivity, and storativity independently.
- [ ] Compare their effects on drawdown.
- [ ] Summarize the most influential parameters for selected scenarios.

**Milestone:** Sensitivity plots with engineering interpretation.

### Phase 4: Uncertainty exploration (optional extension)

- [ ] Define defensible illustrative probability distributions for uncertain inputs.
- [ ] Implement Monte Carlo sampling.
- [ ] Summarize drawdown distributions and selected percentiles.
- [ ] Distinguish uncertainty in aquifer parameters from observation noise.

**Milestone:** Probabilistic drawdown predictions with clearly documented assumptions.

### Phase 5: Calibration and interpretation (optional extension)

- [ ] Generate or obtain pumping-test observations.
- [ ] Estimate transmissivity and storativity using model fitting.
- [ ] Compare fitted and reference parameters.
- [ ] Discuss model limitations and parameter identifiability.

**Milestone:** A documented parameter-estimation exercise.

## Proposed project structure

The structure below is a **suggestion**, not a claim about files already present. Start small and add modules as the project grows.

```text
groundwater_drawdown/
├── README.md
├── pyproject.toml
├── uv.lock
├── .python-version
├── .gitignore
├── .gitattributes
├── docs/
│   ├── PROJECT_OVERVIEW.md
│   ├── PROJECT_STRUCTURE.md
│   └── development_log.md
├── data/
│   └── synthetic/
├── src/
│   └── groundwater_drawdown/
│       ├── __init__.py
│       ├── theis.py
│       └── sensitivity.py
├── experiments/
│   └── run_drawdown.py
├── tests/
│   └── test_theis.py
└── results/
    └── figures/
```

Suggested responsibilities:

- `src/groundwater_drawdown/theis.py`: reusable deterministic drawdown calculations.
- `src/groundwater_drawdown/sensitivity.py`: parameter-sensitivity calculations when needed.
- `experiments/run_drawdown.py`: interactive experiments and plots in Spyder.
- `tests/test_theis.py`: numerical and physical-behavior checks.
- `docs/development_log.md`: decisions, debugging notes, and lessons learned.
- `results/figures/`: exported figures; avoid committing large generated outputs unnecessarily.

For the first milestone, **one experiment script and one calculation module are enough**. Don't create architecture for features that don't exist yet.

## Python environment

The project uses **uv** for Python dependency management and **Spyder** as the interactive development environment.

Example setup for a new project on Windows:

```bash
uv init groundwater_drawdown
cd groundwater_drawdown
uv python pin 3.12
uv add numpy scipy matplotlib
uv add --dev pytest
uv add --dev spyder-kernels
```

If the repository already contains a `pyproject.toml` and `uv.lock`, use:

```bash
uv sync
```

To connect Spyder to this environment, configure its Python interpreter to use:

```text
<project-folder>\.venv\Scripts\python.exe
```

In Spyder, navigate to **Tools → Preferences → Python Interpreter**, select the project interpreter, and restart the IPython console. Use a `spyder-kernels` version compatible with your installed Spyder release if prompted.

> Keep `.venv/`, `.spyproject/`, Python caches, and temporary files out of version control. Commit `pyproject.toml`, `uv.lock`, and `.python-version`.

## Validation approach

The model should be tested against the analytical solution and basic physical expectations:

1. **Zero pumping:** zero drawdown when $Q=0$.
2. **Pumping-rate proportionality:** doubling $Q$ doubles predicted drawdown with other inputs fixed.
3. **Time behavior:** drawdown increases with pumping duration at fixed positive distance under the idealized model.
4. **Distance behavior:** drawdown decreases with increasing distance at fixed time.
5. **Numerical agreement:** selected outputs match an independent benchmark within a stated tolerance.
6. **Input handling:** invalid values are rejected or documented consistently.

Record test parameters, expected results, and units. A plausible-looking graph is not sufficient validation.

## Expected outputs

As the project develops, expected outputs include:

- Single-point drawdown calculations.
- Drawdown-versus-time plots.
- Radial drawdown profiles.
- Parameter-sensitivity comparisons.
- Optional Monte Carlo distributions and calibration diagnostics.
- A short explanation of what each result means physically.

## Learning objectives

This project emphasizes independent scientific programming:

- Translating governing equations into Python functions.
- Working with NumPy arrays and SciPy special functions.
- Creating and interpreting scientific plots.
- Debugging calculations with Spyder's Variable Explorer.
- Testing numerical behavior and managing units.
- Separating reusable model logic from experiments.
- Documenting assumptions, limitations, and engineering interpretations.

AI may be used for conceptual explanations, code review, and debugging guidance. The core numerical implementation is intended to be written and understood by the project author.

## References

- [SciPy `scipy.special.exp1` documentation](https://docs.scipy.org/doc/scipy/reference/generated/scipy.special.exp1.html)
- [Spyder documentation](https://docs.spyder-ide.org/)
- [uv documentation](https://docs.astral.sh/uv/)

## Project status

**In development.** The immediate target is Phase 1: implement and validate the deterministic Theis drawdown calculation at a single observation point.
