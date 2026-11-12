# Groundwater Drawdown Simulator

## Project overview

**Project type:** Standalone scientific Python application  
**Primary environment:** Spyder IDE  
**Environment management:** `uv`  
**Domain:** Hydrogeology, groundwater hydraulics, numerical/scientific computing, digital twin modeling  
**Initial difficulty:** Beginner–intermediate  
**Advanced extensions:** Monte Carlo uncertainty analysis and groundwater digital twin modeling  
**Development approach:** Independently implement the physics and calculations; use assistance for conceptual guidance, review, and debugging.

## 1. Problem statement

Groundwater withdrawals from a pumping well lower hydraulic head in the surrounding aquifer. The resulting **drawdown** varies with pumping duration, distance from the well, and aquifer hydraulic properties. Understanding this response is fundamental to assessing well interference, monitoring-well response, and the limitations of simplified groundwater models.

This project will develop a Python simulator that calculates and visualizes transient drawdown around a **single constant-rate pumping well in an ideal confined aquifer**, using the analytical Theis solution. The program should allow a user to vary pumping rate, transmissivity, storativity, time, and radial distance, then interpret how those inputs affect the predicted response.

The initial objective is not to create a regulatory or design-grade groundwater model. It is to translate a physical model into independently written, tested, and interpretable scientific software.

Following verification of the deterministic simulator, the project may be extended to investigate uncertainty in aquifer parameters through Monte Carlo simulation.

A subsequent advanced phase will investigate **groundwater digital twin modeling** by integrating the physics-based simulator with synthetic observation-well measurements, parameter estimation, model calibration, and sequential model updating.

The digital twin extension will demonstrate how a computational representation of an aquifer can be updated using observations. It will initially use synthetic measurements rather than live monitoring data and will not represent a field-validated groundwater system.

## 2. Central scientific question

**How does drawdown in a confined aquifer change over time and distance from a pumping well, and how sensitive are the predictions to pumping rate, transmissivity, and storativity?**

Supporting questions:

- How does drawdown at a fixed observation well evolve after pumping begins?
- How does drawdown vary with radial distance at a selected time?
- What is the effect of increasing or decreasing pumping rate?
- How do transmissivity and storativity change the shape of the drawdown response?
- When do the assumptions of the analytical solution limit its applicability?
- How does uncertainty in aquifer parameters affect predicted drawdown?
- How can observation-well measurements be used to estimate aquifer parameters?
- How can new observations be incorporated into a physics-based model to update predictions?
- How do measurement uncertainty and model assumptions influence digital twin predictions?

## 3. Scientific basis

### 3.1 Theis solution

For an ideal confined aquifer, the transient drawdown is

$$
s(r,t)=\frac{Q}{4\pi T}W(u)
$$

where

$$
u=\frac{r^2S}{4Tt}
$$

and

$$
W(u)=E_1(u)=\int_u^\infty\frac{e^{-y}}{y}\,dy.
$$

| Symbol | Meaning | Example units |
|---|---|---|
| \(s\) | Drawdown | m |
| \(Q\) | Constant pumping discharge | m³/day |
| \(T\) | Aquifer transmissivity | m²/day |
| \(S\) | Dimensionless storativity | – |
| \(r\) | Radial distance from pumping well | m |
| \(t\) | Time since pumping began | day |
| \(W(u)\) | Theis well function | – |

Use `scipy.special.exp1(u)` to evaluate the exponential integral. The scientific implementation should still explicitly compute \(u\), the well function, and drawdown so that the physics remains visible in the independently developed code.

### 3.2 Initial modeling assumptions

- Confined aquifer of effectively infinite lateral extent.
- Homogeneous, isotropic aquifer of uniform thickness.
- Constant pumping rate beginning at time zero.
- Fully penetrating ideal pumping well; negligible wellbore storage and skin effects.
- Horizontal radial flow governed by Darcy's law.
- Constant transmissivity and storativity; no recharge, leakage, or boundary effects.
- Drawdown evaluated at positive radial distance and positive elapsed time.

These assumptions must accompany any results.

In particular, **do not evaluate the idealized solution at \(r=0\)**, and avoid interpreting it as a prediction of actual water level inside a finite-diameter pumping well.

### 3.3 Digital twin scientific foundation

A groundwater digital twin is a computational representation of a groundwater system that incorporates observations to maintain or update its representation of the physical system.

For this project, the digital twin will use the Theis analytical solution as its physics-based modeling component.

The initial digital twin prototype will consist of:

1. **Physical system representation:** A hypothetical confined aquifer containing a single constant-rate pumping well and one or more observation wells.
2. **Physics-based model:** The independently implemented Theis solution.
3. **Observation data:** Synthetic time-series measurements of drawdown at selected observation wells.
4. **Parameter estimation:** Numerical methods for estimating transmissivity and storativity from observations.
5. **Model updating:** Recalibration or updating of model parameters as additional observations become available.
6. **Prediction and visualization:** Comparison of observed, initial predicted, and updated predicted drawdown.

The digital twin will initially operate in an offline, batch-processing environment.

The project will distinguish between:

- **Simulation:** Predicting system behavior using specified model parameters.
- **Calibration:** Estimating model parameters from observed system behavior.
- **Model updating:** Incorporating additional observations to revise parameter estimates or predictions.
- **Digital twin:** A model-based representation linked to observations through a repeatable updating process.

A synthetic-data digital twin prototype does not establish that the model accurately represents an actual aquifer.

Field validation would require appropriate observations from a physical groundwater system.

## 4. Project objectives

1. Implement the governing analytical equations as reusable Python functions.
2. Define and validate model inputs, including physical units and allowable ranges.
3. Compute drawdown at a single observation location and across arrays of times or distances.
4. Visualize time–drawdown curves and radial drawdown profiles.
5. Explore sensitivity to pumping rate, transmissivity, and storativity.
6. Verify calculations against independent reference values and physical expectations.
7. Document assumptions, interpretation, limitations, and what was learned during development.
8. Investigate uncertainty in aquifer parameters using Monte Carlo simulation.
9. Develop a prototype groundwater digital twin using the verified analytical simulator.
10. Generate reproducible synthetic observation-well measurements.
11. Investigate numerical parameter estimation and model calibration.
12. Demonstrate sequential model updating as additional observations become available.
13. Evaluate prediction residuals, parameter uncertainty, and digital twin limitations.

Objectives 1–7 define the core deterministic project.

Objective 8 represents the optional uncertainty extension.

Objectives 9–13 represent the advanced digital twin extension.

## 5. Scope and development phases

### Phase 1 — Deterministic single-point model

**Task:** Compute drawdown for one set of \(Q,T,S,r,t\).

**Implementation goals:**

- Write functions to calculate \(u\) and \(s\).
- Enforce positive \(T,S,r,t\) and nonnegative \(Q\).
- Use a consistent unit system.
- Keep the mathematical implementation independent of visualization code.

**Deliverable:** A script that prints labeled inputs and calculated drawdown, with units.

**Acceptance criteria:**

- Zero pumping yields zero drawdown.
- Positive pumping yields finite, nonnegative drawdown for valid inputs.
- Invalid inputs produce clear errors.

### Phase 2 — Time–drawdown analysis

**Task:** Compute drawdown at one observation well over a user-defined time range.

**Implementation goals:**

- Generate time arrays with NumPy.
- Calculate vectorized results.
- Plot drawdown versus time.
- Use a logarithmic time axis where appropriate.

**Deliverable:** A labeled time–drawdown plot and a table or CSV of calculated values.

**Acceptance criteria:** At a fixed positive radius, drawdown increases with pumping time under the assumed model.

### Phase 3 — Radial drawdown profiles

**Task:** Calculate drawdown versus distance at one or more pumping durations.

**Implementation goals:**

- Generate positive radial-distance arrays.
- Compare profiles for selected times.
- Visualize the modeled cone of depression.

**Deliverable:** Radial drawdown plots illustrating the modeled cone of depression.

**Acceptance criteria:**

- At fixed time, drawdown decreases as radial distance increases.
- Explain why the idealized model is not evaluated at the well center.

### Phase 4 — Parameter sensitivity

**Task:** Compare model outputs for controlled changes in \(Q\), \(T\), and \(S\).

**Implementation goals:**

- Change one parameter at a time while holding the others fixed.
- Produce comparison figures.
- Summarize the physical interpretation of parameter changes.

**Deliverable:** Sensitivity plots and a brief technical interpretation.

**Acceptance criteria:**

- Doubling \(Q\) doubles drawdown when all other inputs are unchanged.
- Document the less-direct effects of \(T\) and \(S\).

### Phase 5 — Optional uncertainty extension

**Task:** Introduce uncertain aquifer parameters through Monte Carlo simulation, only after the deterministic model is verified.

**Implementation goals:**

- Assign clearly justified illustrative distributions to selected parameters.
- Sample parameter values using a reproducible random seed.
- Calculate drawdown distributions.
- Investigate the sensitivity of predicted drawdown to uncertain parameters.
- Compare deterministic predictions with uncertainty intervals.

**Deliverables:**

- Histograms of simulated drawdown.
- Selected prediction quantiles.
- Sensitivity plots.
- A discussion of input assumptions and uncertainty.

**Acceptance criteria:**

- Distinguish uncertainty in parameter values from measurement error.
- Do not present arbitrary assumed distributions as field-calibrated estimates.
- Ensure Monte Carlo calculations reproduce the deterministic model when parameter uncertainty is removed.

### Phase 6 — Groundwater Digital Twin Modeling and Simulation

**Task:** Extend the verified groundwater drawdown simulator into a prototype digital twin that integrates the analytical Theis solution with time-dependent observation-well data, model calibration, and updated predictions.

The initial digital twin will represent a hypothetical confined aquifer containing a single constant-rate pumping well and one or more observation wells.

Synthetic observations will be used to demonstrate model updating and calibration before introducing actual pumping-test measurements.

#### 6.1 Digital twin framework

**Implementation goals:**

- Use the existing Theis simulator as the physics-based modeling component.
- Define the relationship between aquifer parameters, pumping operations, observation-well measurements, and model predictions.
- Establish consistent representations of simulation time, observation locations, and physical units.
- Separate the physical model, observation data, parameter estimation, and visualization components.
- Establish a reproducible workflow for incorporating additional observations.

**Deliverable:** A documented digital twin architecture and modular Python implementation.

#### 6.2 Synthetic observation-well data

**Implementation goals:**

- Generate synthetic drawdown measurements at selected observation wells.
- Introduce documented measurement noise to represent observational uncertainty.
- Optionally introduce missing measurements or irregular sampling intervals.
- Preserve the true simulation parameters separately from parameters used for estimation.
- Record timestamps, observation-well locations, units, and data provenance.
- Use reproducible random seeds.

**Deliverable:** A synthetic observation-well dataset with supporting metadata and generation documentation.

**Acceptance criteria:**

- Synthetic observations are reproducible.
- True model parameters remain available for verification.
- Measurement noise is explicitly documented.
- Synthetic measurements are clearly distinguished from field observations.

#### 6.3 Parameter estimation and model calibration

**Implementation goals:**

- Compare predicted drawdown with synthetic observations.
- Investigate parameter estimation for transmissivity and storativity.
- Use numerical optimization methods, such as `scipy.optimize.least_squares`, to minimize residuals between modeled and observed drawdown.
- Evaluate the sensitivity of calibration results to initial parameter estimates.
- Investigate parameter identifiability and the influence of measurement noise.
- Compare estimated parameters with the known synthetic parameters.

**Deliverables:**

- Parameter estimation functions.
- Calibration experiment scripts.
- Tables comparing true and estimated parameters.
- Residual plots and calibration statistics.

**Acceptance criteria:**

- Calibration demonstrates reasonable recovery of known parameters under suitable synthetic conditions.
- Parameter estimates remain within physically meaningful ranges.
- Calibration residuals are calculated and documented.
- Limitations associated with measurement noise and parameter identifiability are discussed.

#### 6.4 Sequential model updating

**Implementation goals:**

- Introduce additional observations sequentially.
- Reestimate model parameters as new measurements become available.
- Compare initial predictions with updated predictions.
- Investigate how additional observations influence parameter uncertainty.
- Evaluate predictions against observations withheld from calibration.
- Preserve the history of parameter estimates and model updates.

**Deliverables:**

- A sequential model updating experiment.
- Parameter estimate histories.
- Comparisons of initial and updated predictions.
- Prediction residuals for withheld observations.

**Acceptance criteria:**

- Additional observations can be incorporated without changing the governing equations.
- Model updates are reproducible.
- Changes in parameter estimates and predictions are documented.
- Updated model performance is evaluated using observations not included in the corresponding calibration step.

#### 6.5 Digital twin visualization

**Implementation goals:**

- Plot observed and predicted drawdown over time.
- Compare initial and calibrated model responses.
- Display prediction residuals and parameter estimates.
- Illustrate how updated parameters influence future drawdown predictions.
- Visualize uncertainty intervals where supported by the selected method.

**Deliverables:**

- Observed-versus-predicted drawdown plots.
- Calibration comparison figures.
- Residual plots.
- Parameter updating plots.
- Prediction uncertainty visualizations, where applicable.

The initial implementation will use Matplotlib within Spyder rather than a web dashboard.

#### 6.6 Digital twin uncertainty and limitations

**Implementation goals:**

- Investigate the sensitivity of calibrated parameters to measurement uncertainty.
- Distinguish parameter uncertainty, observation error, and structural model limitations.
- Examine the limitations of calibrating a model using observations generated from the same governing equations.
- Investigate whether additional observations meaningfully improve parameter estimation.
- Document conditions under which the Theis assumptions may prevent the model from adequately representing an actual aquifer.

**Deliverable:** A technical discussion of digital twin uncertainty, calibration performance, and scientific limitations.

**Acceptance criteria:**

- Synthetic-data calibration is not presented as field validation.
- Measurement uncertainty is documented.
- Parameter estimation limitations are identified.
- The prototype is explicitly described as a synthetic-data digital twin demonstration.
- Any claims regarding improved prediction accuracy are supported by reproducible evaluation results.

### Phase 6 — Overall deliverables

- A modular prototype digital twin using the existing Theis model.
- A reproducible synthetic observation-well dataset.
- Parameter estimation and calibration functions.
- A sequential model updating experiment.
- Plots comparing observations, initial predictions, and updated predictions.
- Calibration residuals and parameter estimation results.
- Automated tests for calibration and updating.
- Technical documentation describing architecture, assumptions, verification, and limitations.

## 6. Data requirements

### 6.1 Initial deterministic model

**No external dataset is required for the initial phases.**

Start with a small, clearly labeled set of hypothetical input parameters.

Keep the initial values in one configuration file or script rather than scattering them throughout the code.

### 6.2 Monte Carlo extension

The uncertainty extension will require:

- Selected probability distributions for uncertain parameters.
- Documented distribution assumptions.
- Random sampling configuration.
- Reproducible random seeds.
- Simulation outputs and summary statistics.

These distributions will initially be illustrative rather than derived from field observations.

### 6.3 Digital twin extension

The digital twin will require synthetic observation-well measurements containing:

- Observation-well identifiers.
- Radial distances from the pumping well.
- Observation timestamps or elapsed pumping times.
- Simulated drawdown measurements.
- Measurement units.
- Measurement noise assumptions.
- Data quality indicators, where applicable.

The dataset generation process must preserve the true simulation parameters for verification while keeping them separate from calibration inputs.

Possible later data sources include published pumping-test examples or field measurements with sufficient metadata on pumping rate, observation distance, units, aquifer conditions, and measurement methods.

Actual field observations are outside the initial digital twin scope.

## 7. Verification and validation plan

Verification asks whether the code correctly implements the equations; validation asks whether the model adequately represents a real physical system.

This project can establish strong **verification**, but field **validation** requires suitable observations.

### 7.1 Deterministic model verification

Recommended checks:

- Independently calculate at least one case using a calculator, spreadsheet, or published example.
- Confirm dimensional consistency: \(Q/T\) has dimensions of length.
- Confirm that \(u\) is dimensionless.
- Test linear scaling with \(Q\).
- Test expected trends with increasing \(t\) and \(r\).
- Check array results against repeated scalar calculations.
- Test input boundaries and errors, including zero or negative \(T,S,r,t\).
- Record the source of every benchmark and the numerical tolerance used.

### 7.2 Monte Carlo verification

Recommended checks:

- Confirm reproducibility with a fixed random seed.
- Verify that sampled parameters satisfy physical constraints.
- Compare selected sampled calculations against deterministic calculations.
- Confirm that zero parameter uncertainty produces deterministic results.
- Document the sensitivity of results to assumed distributions.

### 7.3 Digital twin verification

Recommended checks:

- Confirm that synthetic observations are generated reproducibly.
- Verify observation timestamps, distances, and units.
- Test parameter estimation against known synthetic parameters.
- Evaluate calibration residuals.
- Test calibration sensitivity to starting parameter estimates.
- Confirm that sequential updating uses only observations available at each update.
- Evaluate updated predictions against withheld observations.
- Confirm that calibration and updating do not modify the independently verified Theis equations.
- Document numerical tolerances and optimization convergence criteria.

### 7.4 Validation limitations

The digital twin will initially use synthetic observations generated from the same analytical model used for prediction.

Successful calibration against these observations demonstrates parameter estimation and software functionality under controlled conditions.

It does not establish that the model accurately represents a real aquifer.

Field validation would require suitable groundwater measurements and an assessment of whether the Theis assumptions adequately represent the physical system.

## 8. Required deliverables

### 8.1 Core deterministic simulator

- Reusable Theis-model functions written independently.
- A reproducible experiment script runnable in Spyder.
- Time–drawdown and radial drawdown figures.
- Basic automated tests.
- A README explaining setup, model assumptions, and how to run the simulation.
- A development log describing decisions, mistakes, fixes, and lessons learned.

### 8.2 Optional Monte Carlo extension

- Reproducible uncertainty simulation.
- Documented parameter distributions.
- Drawdown probability distributions and selected quantiles.
- Sensitivity analysis and technical interpretation.

### 8.3 Advanced digital twin extension

- A documented groundwater digital twin architecture.
- Synthetic observation-well data and generation methodology.
- Parameter estimation and calibration functions.
- A sequential model updating workflow.
- Observed-versus-predicted drawdown plots.
- Parameter estimate and calibration residual reports.
- Verification tests.
- Documentation of scientific assumptions and limitations.

## 9. Out of scope

The following remain outside the initial project scope:

- Unconfined or leaky aquifer solutions.
- Multiple interacting pumping wells.
- Recharge, finite boundaries, heterogeneity, anisotropy, or partially penetrating wells.
- Finite-difference groundwater flow solvers or MODFLOW integration.
- Calibration to field data in the initial release.
- Web interfaces, dashboards, APIs, databases, or deployment.
- Live observation-well sensor integration.
- Real-time operational synchronization.
- Automated pumping control.
- Production-grade digital twin infrastructure.
- Claims of field-validated predictive accuracy without suitable observations.

The digital twin extension will focus on an offline, reproducible, physics-based model updating workflow.

## 10. Definition of done

### 10.1 Core deterministic project

The initial project is complete when the developer can:

1. Run a deterministic Theis simulation.
2. Generate and interpret time–drawdown plots.
3. Generate and interpret radial drawdown profiles.
4. Explain the governing assumptions.
5. Demonstrate basic verification tests.
6. Explain the effects of pumping rate, transmissivity, and storativity.
7. Walk through independently written code without relying on an AI-generated implementation.

### 10.2 Monte Carlo extension

The uncertainty extension is complete when the developer can:

1. Define documented illustrative parameter distributions.
2. Generate reproducible random samples.
3. Calculate and visualize drawdown distributions.
4. Interpret selected quantiles and sensitivity results.
5. Explain the limitations of the assumed uncertainty model.

### 10.3 Digital twin extension

The digital twin extension is complete when the developer can:

1. Explain the distinction between a simulation and a digital twin.
2. Generate reproducible synthetic observation-well measurements.
3. Calibrate transmissivity and storativity using observation data.
4. Compare initial and calibrated model predictions.
5. Incorporate additional observations through sequential model updating.
6. Evaluate updated predictions against withheld observations.
7. Visualize model predictions, observations, residuals, and parameter estimates.
8. Explain measurement uncertainty, parameter uncertainty, and structural model limitations.
9. Demonstrate automated verification tests.
10. Walk through the independently developed digital twin implementation and explain the scientific reasoning behind its components.

The completed advanced project will demonstrate a **synthetic-data, physics-based groundwater digital twin prototype**, not a production-ready or field-validated groundwater modeling system.

## 11. Suggested references

### Scientific computing

- [SciPy `scipy.special.exp1` documentation](https://docs.scipy.org/doc/scipy/reference/generated/scipy.special.exp1.html)
- [SciPy `scipy.optimize.least_squares` documentation](https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.least_squares.html)
- [NumPy documentation](https://numpy.org/doc/stable/)
- [Spyder documentation](https://docs.spyder-ide.org/)

### Groundwater science

- [USGS groundwater publications](https://pubs.usgs.gov/)
- Theis, C. V. (1935). The relation between the lowering of the piezometric surface and the rate and duration of discharge of a well using ground-water storage. *Transactions, American Geophysical Union, 16*(2), 519–524.

### Digital twin and model calibration

- [National Institute of Standards and Technology (NIST)](https://www.nist.gov/)
- [SciPy optimization documentation](https://docs.scipy.org/doc/scipy/reference/optimize.html)

When introducing a published numerical benchmark, calibration method, or digital twin framework, cite the specific source and its assumptions rather than relying on a generic reference page.

---

*Status: Project scope and proposed methodology. The deterministic simulator is the initial development priority. Monte Carlo uncertainty analysis and digital twin modeling are planned advanced extensions. Implementation and empirical validation remain future work.*
