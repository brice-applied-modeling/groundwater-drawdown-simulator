# Groundwater Drawdown Simulation High Level Checklist

## 1. Understand the engineering problem
- [ ] Explain what happens to groundwater levels when a well begins pumping
- [ ] Identify pumping rate (Q), transmissivity (T), storativity (S), radial distance (r), and elapsed time (t)
- [ ] Understand the difference between drawdown and hydraulic head
- [ ] Review the assumptions of the Theis confined-aquifer solution
- [ ] Choose one hypothetical pumping scenario and consistent units

## 2. Set up the Spyder project
- [x] Create or open the groundwater_drawdown repository in Spyder
- [x] Initialize the uv environment and confirm the Python interpreter
- [x] Install NumPy, SciPy, Matplotlib, and pytest
- [x] Verify Spyder's IPython console uses the project's interpreter
- [x] Create src/, experiments/, tests/, and results/ folders
- [ ] Run a basic Python script successfully

## 3. Implement the deterministic model
- [ ] Define the five required model inputs
- [ ] Calculate the dimensionless Theis parameter u
- [ ] Evaluate the well function using scipy.special.exp1
- [ ] Calculate drawdown using the Theis equation
- [ ] Write a reusable function with clear arguments and return value
- [ ] Add basic input validation for physically valid values
- [ ] Print and interpret one drawdown result

## 4. Explore drawdown over time and distance
- [ ] Create an array of positive elapsed times with NumPy
- [ ] Calculate drawdown for each time value
- [ ] Plot drawdown against time, preferably with a logarithmic time axis
- [ ] Calculate drawdown at several radial distances
- [ ] Plot and label a drawdown-versus-distance curve
- [ ] Explain what each plot means physically

## 5. Validate the model
- [ ] Compare one result against an independently calculated reference value
- [ ] Confirm drawdown increases with pumping rate
- [ ] Confirm drawdown decreases with radial distance
- [ ] Confirm drawdown increases with elapsed pumping time
- [ ] Check sensitivity to transmissivity and storativity
- [ ] Write automated tests for key numerical and physical behaviors
- [ ] Document assumptions and limitations

## 6. Add sensitivity analysis
- [ ] Define reasonable illustrative ranges for T and S
- [ ] Vary one parameter at a time while holding others fixed
- [ ] Plot comparisons of drawdown curves
- [ ] Identify which inputs most influence predictions
- [ ] Summarize the engineering implications in Markdown

## 7. Optional Monte Carlo extension
- [ ] Assign defensible probability distributions to uncertain parameters
- [ ] Generate samples using NumPy's random generator
- [ ] Run the deterministic model repeatedly
- [ ] Plot the resulting drawdown distribution
- [ ] Calculate selected percentiles and threshold exceedance probability
- [ ] Document why the assumed distributions are appropriate

## 8. Finish and document the project
- [ ] Refactor calculations into reusable modules
- [ ] Keep experiment scripts separate from scientific functions
- [ ] Run tests and inspect plots for correctness
- [ ] Update the README with actual completed capabilities
- [ ] Document lessons learned and remaining limitations
- [ ] Commit the completed work to Git

## Phase 1 Workflow

For the first few sessions, use a single experiment script, such as
`experiments/01_deterministic/run_drawdown.py`. Write the calculations,
execute them, and inspect intermediate values in Spyder's Variable Explorer.

Once the calculation works and is understood, move the reusable mathematics
into a function in `src/groundwater_drawdown/models/theis.py`. This allows for
practice in writing functions, imports, and modular code while maintaining the
planned project architecture.

## What counts as completing Phase 1?

The first meaningful milestone is achieved when the following is achieved:

- [ ] Able to explain the Theis equation and its assumptions.
- [ ] Write a Python function that calculates drawdown.
- [ ] Call that function with different inputs.
- [ ] Produce a drawdown-versus-time plot.
- [ ] Verify the results against a reference calculation.
- [ ] Explain why the resulting curve behaves as it does.

That's a complete, useful scientific programming accomplishment in its own right.

## Suggested first coding session

Work only through Phases 1–3 of the development checklist, stopping once
a validated single-point drawdown calculation has been completed. Don't rush
into Monte Carlo just because it's more interesting. The deterministic model is
the foundation everything else will depend on.
