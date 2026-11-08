# Groundwater Drawdown Simulator

**Scientific Python | Groundwater Hydraulics | Numerical Modeling | Applied Engineering Analytics**

![Project Status](https://img.shields.io/badge/status-in%20development-yellow)
![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python&logoColor=white)
![IDE](https://img.shields.io/badge/IDE-Spyder-red)
![Package Manager](https://img.shields.io/badge/package%20manager-uv-purple)
![Scientific Computing](https://img.shields.io/badge/focus-scientific%20computing-teal)

> **Status:** In development. This repository documents an independent engineering research and scientific computing project developed primarily using Python and Spyder. Features described below are planned unless explicitly marked complete.

## Project Overview

Groundwater pumping lowers hydraulic head in the surrounding aquifer. The resulting drawdown changes over time and varies with distance from the pumping well.

This project investigates that behavior using the **Theis analytical solution** for transient radial flow toward a pumping well in an ideal confined aquifer.

The initial objective is to independently research the engineering principles, implement and verify a deterministic Python model, and develop scientific visualizations that support interpretation of the results.

Later phases may incorporate parameter sensitivity, uncertainty propagation, aquifer parameter calibration, and Bayesian inference.

The project is a standalone scientific computing application, **not a web application or regulatory groundwater design tool**.

## Project Motivation and Background

My professional background is in civil engineering, primarily municipal water, wastewater, and infrastructure engineering. Although I have extensive experience in these disciplines, I have not previously worked in groundwater modeling.

I selected this project deliberately to explore an unfamiliar engineering discipline while continuing to develop my capabilities in Python, scientific computing, mathematical modeling, and applied analytics.

Rather than beginning with the Python implementation, I am approaching the project by first researching and documenting the underlying groundwater hydraulics, governing equations, mathematical assumptions, and limitations of the analytical model.

This approach serves two objectives:

1. **Engineering development:** Establish an independent understanding of groundwater flow and transient drawdown before implementing the mathematical model.
2. **Scientific software development:** Translate that understanding into modular, tested, reproducible Python software capable of supporting increasingly sophisticated numerical and statistical analyses.

The project also provides an opportunity to demonstrate how established engineering experience can be applied to a new technical domain through independent research, computational modeling, and engineering judgment.

The emphasis is on understanding and verifying the scientific calculations rather than developing a graphical application or dashboard.

### Independent Research and Development

The engineering research and core numerical implementation are intended to be completed independently.

AI-assisted tools may be used for documentation review, conceptual clarification, software architecture discussions, debugging guidance, and code review. They are not intended to substitute for independently developing an understanding of the governing engineering principles.

The objective is not simply to produce functioning software, but to understand the physical and mathematical behavior represented by the software.

## Problem Statement

For a confined aquifer pumped at a constant rate, how does groundwater drawdown vary with:

- Elapsed pumping time, $t$?
- Radial distance from the pumping well, $r$?
- Aquifer transmissivity, $T$?
- Aquifer storativity, $S$?
- Pumping rate, $Q$?

The project will calculate drawdown under specified assumptions, visualize the results, and evaluate whether the model behaves consistently with the governing equation and expected groundwater response.

## Scientific Foundation

The Theis solution expresses drawdown as:

$$
s(r,t) = \frac{Q}{4\pi T} W(u)
$$

where:

$$
u = \frac{r^2 S}{4Tt}
$$

and the well function is:

$$
W(u) = E_1(u) = \int_u^\infty \frac{e^{-x}}{x}\,dx
$$

| Symbol | Meaning | Example consistent SI units |
|---|---|---|
| $s$ | Drawdown | m |
| $Q$ | Constant pumping rate | m³/day |
| $T$ | Transmissivity | m²/day |
| $S$ | Storativity | Dimensionless |
| $r$ | Radial distance from pumping well | m |
| $t$ | Time since pumping began | days |
| $W(u)$ | Theis well function | Dimensionless |

**Unit consistency is essential.** For the example units above, time is expressed in days, radial distance in meters, and pumping rate in m³/day.

SciPy provides the exponential integral through `scipy.special.exp1`.

### Modeling Assumptions

The initial model assumes:

- A confined aquifer of effectively infinite areal extent.
- Homogeneous, isotropic aquifer properties with constant transmissivity and storativity.
- A fully penetrating pumping well with constant discharge.
- Horizontal radial flow governed by the idealized Theis formulation.
- Negligible wellbore storage, well losses, recharge, leakage, and boundary effects.
- Drawdown evaluated at positive radial distances and positive elapsed times.

These assumptions limit applicability to real groundwater systems.

The model is intended for scientific education, computational experimentation, and applied modeling research. It is not intended for engineering design without additional site-specific analysis and verification.

### Engineering Background Documentation

The engineering principles underlying this project are being researched and documented separately from the Python implementation.

The engineering background document is intended to establish the physical principles, terminology, mathematical formulation, assumptions, and limitations of the model.

**Engineering background:** `docs/engineering_background.md`

This separation allows the engineering research to develop independently of the software architecture and implementation.

## Development Roadmap

### Phase 1: Single-Point Deterministic Calculation

- [ ] Define inputs and their units.
- [ ] Implement a function that calculates $u$, $W(u)$, and drawdown.
- [ ] Validate input domains, including $T>0$, $S>0$, $r>0$, $t>0$, and an appropriate nonnegative pumping rate.
- [ ] Calculate drawdown at one observation point.
- [ ] Compare the result with an independent reference calculation.
- [ ] Develop automated numerical tests.

**Milestone:** A reproducible, verified single-point calculation.

### Phase 2: Drawdown Over Time and Distance

- [ ] Evaluate drawdown over a sequence of pumping times.
- [ ] Evaluate drawdown at multiple radial distances.
- [ ] Plot drawdown versus time and distance using Matplotlib.
- [ ] Label axes and document units.
- [ ] Investigate expected trends and limiting behavior.
- [ ] Interpret the results in terms of groundwater hydraulics.

**Milestone:** Interpretable drawdown curves and a radial drawdown profile.

### Phase 3: Parameter Sensitivity

- [ ] Vary pumping rate, transmissivity, and storativity independently.
- [ ] Compare their effects on drawdown.
- [ ] Evaluate parameter sensitivity across selected scenarios.
- [ ] Document the engineering interpretation of the results.

**Milestone:** Sensitivity plots with engineering interpretation.

### Phase 4: Uncertainty Exploration (Optional Extension)

- [ ] Define defensible illustrative probability distributions for uncertain inputs.
- [ ] Implement Monte Carlo sampling.
- [ ] Summarize drawdown distributions and selected percentiles.
- [ ] Distinguish uncertainty in aquifer parameters from observation noise.
- [ ] Evaluate the influence of uncertainty assumptions on model predictions.

**Milestone:** Probabilistic drawdown predictions with clearly documented assumptions.

### Phase 5: Calibration and Interpretation (Optional Extension)

- [ ] Generate or obtain pumping-test observations.
- [ ] Estimate transmissivity and storativity using model fitting.
- [ ] Compare fitted and reference parameters.
- [ ] Evaluate residuals and parameter identifiability.
- [ ] Discuss model limitations and interpretation.

**Milestone:** A documented parameter-estimation exercise.

### Phase 6: Bayesian Parameter Estimation (Potential Future Extension)

- [ ] Investigate Bayesian approaches to estimating aquifer parameters.
- [ ] Define prior distributions and an observation-error model.
- [ ] Develop a likelihood function based on the analytical solution.
- [ ] Estimate posterior distributions for transmissivity and storativity.
- [ ] Evaluate posterior predictive uncertainty.
- [ ] Compare Bayesian results with conventional calibration.

**Milestone:** A documented Bayesian parameter-estimation and predictive uncertainty analysis.

## Proposed Project Structure

The project structure documented in the architecture directory represents the anticipated organization of the repository. Additional modules and directories will be introduced as development progresses.
The proposed repository organization, including directory structure and module responsibilities, is documented in the [Project Structure](docs/01_architecture/00_project_structure.md).

### Module Responsibilities

The project follows a modular architecture that separates groundwater modeling, numerical computations, parameter estimation, uncertainty analysis, visualization, and experimental workflows.

#### Core Scientific Modules

- `src/groundwater_drawdown/models/`: Contains the analytical groundwater models, beginning with the Theis solution implemented in `theis.py`.
- `src/groundwater_drawdown/numerical/`: Provides supporting numerical methods and computational utilities required by the groundwater models.
- `src/groundwater_drawdown/calibration/`: Supports estimation of aquifer parameters using observed or synthetic pumping-test data.
- `src/groundwater_drawdown/uncertainty/`: Supports probabilistic modeling, Monte Carlo simulation, and uncertainty quantification.
- `src/groundwater_drawdown/analysis/`: Contains sensitivity analysis and other methods for evaluating model behavior.
- `src/groundwater_drawdown/visualization/`: Generates scientific figures and graphical representations of simulation results.
- `src/groundwater_drawdown/utils/`: Contains shared utility functions used throughout the application.

#### Experimental Workflows

The `experiments/` directory separates executable scientific experiments by modeling approach.

- `01_deterministic/`: Initial deterministic groundwater drawdown calculations.
- `02_sensitivity/`: Investigation of parameter sensitivity and model response.
- `03_calibration/`: Aquifer parameter estimation and calibration experiments.
- `04_monte_carlo/`: Probabilistic simulations and uncertainty propagation.
- `05_bayesian/`: Bayesian parameter estimation and posterior predictive analysis.

#### Testing and Verification

The `tests/` directory organizes automated tests according to the scientific components being evaluated.

- `test_models/`: Verification of analytical groundwater model calculations.
- `test_numerical/`: Verification of supporting numerical computations.
- `test_calibration/`: Testing parameter-estimation methods and calibration workflows.
- `test_uncertainty/`: Testing probabilistic simulations and uncertainty calculations.

#### Engineering and Project Documentation

The `docs/` directory contains the project documentation, organized by subject.

- `00_overview/`: Project objectives, scope, and overall development approach.
- `01_architecture/`: Repository architecture, directory organization, and module responsibilities.
- `02_engineering_documentation/`: Groundwater engineering research, mathematical background, model assumptions, initial test scenarios, validation planning, and development records.
- `03_checklists/`: Development checklists and milestone tracking.

#### Data Management

The `data/` directory separates datasets according to their origin and processing status.

- `raw/`: Original source datasets retained without modification.
- `synthetic/`: Artificially generated datasets used for testing, calibration, and experimentation.
- `processed/`: Cleaned or transformed datasets prepared for analysis.

#### Simulation Results

The `results/` directory organizes generated scientific outputs.

- `figures/`: Scientific plots and visualizations.
- `tables/`: Tabulated simulation results and numerical summaries.
- `reports/`: Generated analytical reports and experiment summaries.

### Development Approach

The project architecture is designed to accommodate future scientific modeling capabilities without requiring all components to be implemented immediately.

Development will begin with the deterministic Theis model. Additional numerical methods, analytical workflows, calibration routines, and uncertainty analysis capabilities will be introduced progressively as the project advances.

The initial priority remains developing, understanding, and verifying the core groundwater drawdown calculations before expanding into more advanced modeling techniques.

## Python Environment

The project uses **uv** for Python dependency management and **Spyder** as the primary interactive development environment.

Example setup for a new project on Windows:

```bash
uv init groundwater_drawdown
cd groundwater_drawdown
uv python pin 3.12
uv add numpy scipy matplotlib
uv add --dev pytest
uv add --dev spyder-kernels
```

For an existing repository containing `pyproject.toml` and `uv.lock`:

```bash
uv sync
```

To connect Spyder to the project environment, configure its Python interpreter to use:

```text
<project-folder>\.venv\Scripts\python.exe
```

In Spyder, navigate to **Tools → Preferences → Python Interpreter**, select the project interpreter, and restart the IPython console.

Use a `spyder-kernels` version compatible with the installed Spyder release.

> Keep `.venv/`, `.spyproject/`, Python caches, and temporary files out of version control. Commit `pyproject.toml`, `uv.lock`, and `.python-version`.

## Verification and Validation Approach

The model will be evaluated using independent numerical calculations, analytical relationships, and expected physical behavior.

Planned checks include:

1. **Zero pumping:** Zero drawdown when $Q=0$.
2. **Pumping-rate proportionality:** Doubling $Q$ doubles predicted drawdown with other inputs fixed.
3. **Time behavior:** Drawdown increases with pumping duration at fixed positive distance under the idealized model.
4. **Distance behavior:** Drawdown decreases with increasing distance at fixed time.
5. **Numerical agreement:** Selected outputs match independently calculated benchmarks within specified tolerances.
6. **Input handling:** Invalid input values are rejected or documented consistently.

Verification activities will document the test parameters, expected results, units, numerical tolerances, and outcomes.

A plausible-looking graph is not sufficient evidence that the model has been implemented correctly.

Verification of the mathematical implementation will also be distinguished from validation of the model's ability to represent actual groundwater systems.

## Expected Outputs

As the project develops, anticipated outputs include:

- Single-point groundwater drawdown calculations.
- Drawdown-versus-time plots.
- Radial drawdown profiles.
- Parameter-sensitivity comparisons.
- Monte Carlo drawdown distributions.
- Aquifer parameter calibration results.
- Potential Bayesian posterior and predictive distributions.
- Engineering interpretations and documented model limitations.

Results will be generated through Python scripts and scientific plotting libraries rather than a web dashboard.

## Learning and Development Objectives

The project combines independent engineering research with scientific software development.

### Engineering and Mathematical Objectives

- Research groundwater hydraulics outside my existing engineering specialization.
- Understand the physical assumptions underlying the Theis solution.
- Investigate transient radial groundwater flow.
- Understand the relationships between aquifer properties and drawdown.
- Evaluate the applicability and limitations of analytical groundwater models.
- Develop engineering interpretations of computational results.

### Python and Scientific Computing Objectives

- Translate governing equations into reusable Python functions.
- Work with NumPy arrays and SciPy mathematical functions.
- Create and interpret scientific visualizations.
- Develop automated numerical tests.
- Debug calculations using Spyder.
- Organize scientific Python code into maintainable modules.
- Develop reproducible computational experiments.

### Advanced Modeling Objectives

Potential future extensions will introduce:

- Sensitivity analysis.
- Numerical parameter estimation.
- Monte Carlo uncertainty propagation.
- Statistical model calibration.
- Bayesian inference.
- Predictive uncertainty quantification.

These extensions are intended to build progressively on the verified deterministic model.

## References

- [SciPy `scipy.special.exp1` documentation](https://docs.scipy.org/doc/scipy/reference/generated/scipy.special.exp1.html)
- [Spyder documentation](https://docs.spyder-ide.org/)
- [uv documentation](https://docs.astral.sh/uv/)

Additional groundwater engineering references will be documented as the engineering research progresses.

## Project Status

**In development.**

The project is currently focused on establishing the engineering background and implementing the first deterministic Theis drawdown calculation.

The immediate technical milestone is a verified calculation at a single observation point.

Subsequent phases will progressively introduce scientific visualizations, parameter sensitivity, uncertainty analysis, and parameter estimation.