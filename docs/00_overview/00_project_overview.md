# Groundwater Drawdown Simulator

## Project overview

**Project type:** Standalone scientific Python application  
**Primary environment:** Spyder IDE  
**Environment management:** `uv`  
**Domain:** Hydrogeology, groundwater hydraulics, numerical/scientific computing  
**Initial difficulty:** Beginner–intermediate  
**Development approach:** Independently implement the physics and calculations; use assistance for conceptual guidance, review, and debugging.

## 1. Problem statement

Groundwater withdrawals from a pumping well lower hydraulic head in the surrounding aquifer. The resulting **drawdown** varies with pumping duration, distance from the well, and aquifer hydraulic properties. Understanding this response is fundamental to assessing well interference, monitoring-well response, and the limitations of simplified groundwater models.

This project will develop a Python simulator that calculates and visualizes transient drawdown around a **single constant-rate pumping well in an ideal confined aquifer**, using the analytical Theis solution. The program should allow a user to vary pumping rate, transmissivity, storativity, time, and radial distance, then interpret how those inputs affect the predicted response.

The objective is not to create a regulatory or design-grade groundwater model. It is to translate a physical model into independently written, tested, and interpretable scientific software.

## 2. Central scientific question

**How does drawdown in a confined aquifer change over time and distance from a pumping well, and how sensitive are the predictions to pumping rate, transmissivity, and storativity?**

Supporting questions:

- How does drawdown at a fixed observation well evolve after pumping begins?
- How does drawdown vary with radial distance at a selected time?
- What is the effect of increasing or decreasing pumping rate?
- How do transmissivity and storativity change the shape of the drawdown response?
- When do the assumptions of the analytical solution limit its applicability?

## 3. Scientific basis

### 3.1 Theis solution

For an ideal confined aquifer, the transient drawdown is

\[
s(r,t)=\frac{Q}{4\pi T}W(u)
\]

where

\[
u=\frac{r^2S}{4Tt}
\]

and

\[
W(u)=E_1(u)=\int_u^\infty\frac{e^{-y}}{y}\,dy.
\]

| Symbol | Meaning | Example units |
|---|---|---|
| \(s\) | Drawdown | m |
| \(Q\) | Constant pumping discharge | m³/day |
| \(T\) | Aquifer transmissivity | m²/day |
| \(S\) | Dimensionless storativity | – |
| \(r\) | Radial distance from pumping well | m |
| \(t\) | Time since pumping began | day |
| \(W(u)\) | Theis well function | – |

Use `scipy.special.exp1(u)` to evaluate the exponential integral. The scientific implementation should still explicitly compute \(u\), the well function, and drawdown so that the physics remains visible in your own code.

### 3.2 Initial modeling assumptions

- Confined aquifer of effectively infinite lateral extent.
- Homogeneous, isotropic aquifer of uniform thickness.
- Constant pumping rate beginning at time zero.
- Fully penetrating ideal pumping well; negligible wellbore storage and skin effects.
- Horizontal radial flow governed by Darcy's law.
- Constant transmissivity and storativity; no recharge, leakage, or boundary effects.
- Drawdown evaluated at positive radial distance and positive elapsed time.

These assumptions must accompany any results. In particular, **do not evaluate the idealized solution at \(r=0\)**, and avoid interpreting it as a prediction of actual water level inside a finite-diameter pumping well.

## 4. Project objectives

1. Implement the governing analytical equations as reusable Python functions.
2. Define and validate model inputs, including physical units and allowable ranges.
3. Compute drawdown at a single observation location and across arrays of times or distances.
4. Visualize time–drawdown curves and radial drawdown profiles.
5. Explore sensitivity to pumping rate, transmissivity, and storativity.
6. Validate calculations against independent reference values and physical expectations.
7. Document assumptions, interpretation, limitations, and what was learned during development.

## 5. Scope and development phases

### Phase 1 — Deterministic single-point model

**Task:** Compute drawdown for one set of \(Q,T,S,r,t\).

**Implementation goals:** Write functions to calculate \(u\) and \(s\); enforce positive \(T,S,r,t\) and nonnegative \(Q\); use a consistent unit system.

**Deliverable:** A script that prints labeled inputs and calculated drawdown, with units.

**Acceptance criteria:** Zero pumping yields zero drawdown; positive pumping yields finite, nonnegative drawdown for valid inputs; invalid inputs produce clear errors.

### Phase 2 — Time–drawdown analysis

**Task:** Compute drawdown at one observation well over a user-defined time range.

**Implementation goals:** Generate time arrays with NumPy, calculate vectorized results, and plot drawdown versus time. A logarithmic time axis is often useful.

**Deliverable:** A labeled time–drawdown plot and a table or CSV of calculated values.

**Acceptance criteria:** At a fixed positive radius, drawdown increases with pumping time under the assumed model.

### Phase 3 — Radial drawdown profiles

**Task:** Calculate drawdown versus distance at one or more pumping durations.

**Implementation goals:** Generate positive radial-distance arrays and compare profiles for selected times.

**Deliverable:** Radial drawdown plots illustrating the modeled cone of depression.

**Acceptance criteria:** At fixed time, drawdown decreases as radial distance increases. Explain why the idealized model is not evaluated at the well center.

### Phase 4 — Parameter sensitivity

**Task:** Compare model outputs for controlled changes in \(Q\), \(T\), and \(S\).

**Implementation goals:** Change one parameter at a time while holding the others fixed; produce comparison figures and summarize observations.

**Deliverable:** Sensitivity plots and a brief technical interpretation.

**Acceptance criteria:** Doubling \(Q\) doubles drawdown when all other inputs are unchanged; document the less-direct effects of \(T\) and \(S\).

### Phase 5 — Optional uncertainty extension

**Task:** Introduce uncertain aquifer parameters through Monte Carlo simulation, only after the deterministic model is verified.

**Implementation goals:** Assign clearly justified illustrative distributions to selected parameters, sample them with a reproducible random seed, and calculate drawdown distributions.

**Deliverable:** Histograms, selected prediction quantiles, and a discussion of input assumptions.

**Acceptance criteria:** Distinguish uncertainty in parameter values from measurement error; do not present arbitrary assumed distributions as field-calibrated estimates.

## 6. Data requirements

**No external dataset is required for the initial phases.** Start with a small, clearly labeled set of hypothetical input parameters. Keep the initial values in one configuration file or script rather than scattering them throughout the code.

Possible later data sources include published pumping-test examples or field measurements with sufficient metadata on pumping rate, observation distance, units, and aquifer conditions. Such data are outside the initial scope.

## 7. Verification and validation plan

Verification asks whether the code correctly implements the equations; validation asks whether the model adequately represents a real physical system. This project can establish strong **verification**, but field **validation** requires suitable observations.

Recommended checks:

- Independently calculate at least one case using a calculator, spreadsheet, or published example.
- Confirm dimensional consistency: \(Q/T\) has dimensions of length.
- Confirm that \(u\) is dimensionless.
- Test linear scaling with \(Q\).
- Test expected trends with increasing \(t\) and \(r\).
- Check array results against repeated scalar calculations.
- Test input boundaries and errors, including zero or negative \(T,S,r,t\).
- Record the source of every benchmark and the numerical tolerance used.

## 8. Required deliverables

- Reusable Theis-model functions written by you.
- A reproducible experiment script runnable in Spyder.
- Time–drawdown and radial drawdown figures.
- Basic automated tests.
- A README explaining setup, model assumptions, and how to run the simulation.
- A development log describing decisions, mistakes, fixes, and lessons learned.

**Optional:** Monte Carlo extension and comparison against observed pumping-test data.

## 9. Out of scope

- Unconfined or leaky aquifer solutions.
- Multiple interacting pumping wells.
- Recharge, finite boundaries, heterogeneity, anisotropy, or partially penetrating wells.
- Finite-difference groundwater flow solvers or MODFLOW integration.
- Calibration to field data in the initial release.
- Web interfaces, dashboards, APIs, databases, or deployment.

## 10. Definition of done

The initial project is complete when you can run a deterministic Theis simulation, generate and interpret both required plot types, explain the governing assumptions, demonstrate basic verification tests, and walk through **your own code** without relying on an AI-generated implementation.

## 11. Suggested references

- [SciPy `scipy.special.exp1` documentation](https://docs.scipy.org/doc/scipy/reference/generated/scipy.special.exp1.html)
- [USGS groundwater publications](https://pubs.usgs.gov/)
- [Spyder documentation](https://docs.spyder-ide.org/)

When introducing a published numerical benchmark, cite the specific source and its assumptions rather than relying on a generic reference page.
