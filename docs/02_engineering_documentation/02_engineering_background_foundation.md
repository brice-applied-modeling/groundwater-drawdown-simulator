
# Groundwater Drawdown Engineering Background

The purpose of this document, is to research, understand, and document the
engineering for the problem statement of this project.  Artificial Intelligence (AI)
was only used to help polish, but was not used to produce any of the project
understanding.

## Problem statement

Groundwater withdrawals from a pumping well lower hydraulic head in the
surrounding aquifer. The resulting **drawdown** varies with pumping duration,
distance from the well, and aquifer hydraulic properties. Understanding this
response is fundamental to assessing well interference, monitoring-well response,
and the limitations of simplified groundwater models.

This project will develop a Python simulator that calculates and visualizes
transient drawdown around a **single constant-rate pumping well in an ideal**
**confined aquifer**, using the analytical Theis solution. The program should
allow a user to vary pumping rate, transmissivity, storativity, time, and
radial distance, then interpret how those inputs affect the predicted response.

The objective is not to create a regulatory or design-grade groundwater model.
It is to translate a physical model into independently written, tested, and
interpretable scientific software.

## Define Terminology

- **Drawdown:** The lowering of the water level due to pumping or other means of 
withdrawing the groundwater aquifer.
- **Transmissivity:** The capacity of the aquifer to transmit water{cite:p}`woessner2020_aquifer`
- **Storativity:** The capacity of an aquifer to store or release water. The 
storativity of a confined aquifer remains saturated and unchanged when there is
a unit change in the potentiometric surface {cite:p}`woessner2020_aquifer`.
- **Radial Distance:** Distance from a pumping well to a point in the aquifer
- **Confined Aquifer:** The aquifer is bounded above and below by impermeable
layers, known as aquitards {cite:p}`theis1935`.
- **Homogeneous:** An aquifer's hydraulic properties are uniform throughout its
volume {cite:p}`freeze1979`.
- **Isotropic:** An aquifer's hydraulic properties are the same in all directions
at a given point. This implies that the hydraulic conductivity is independent of
the direction of flow. In an isotropic aquifer, water will flow at the same rate
in any direction, assuming the same hydraulic gradient {cite:p}`freeze1979`.
- **Theis Equation:** A method that provides a mathematical framework for
predicting how water levels in a confined aquifer decline over time due to
pumping from a well {cite:p}`lmno_theis`.
- **Wellbore:** A cylindrical hole drilled into the earth's subsurface, serves
as the crucial conduit for accessing subsurface resources, facilitating a wide
array of operations ranging from oil and gas extraction to geothermal energy
production and groundwater monitoring {cite:p}`flyriver_wellbore`.
- **Wellbore Storage:** refers to the phenomenon where the pressure behavior in
a well is influenced by the compressibility and volume of the fluid within the
wellbore, particularly during the early stages of production or shut-in. This
effect can lead to a time lag in the surface production rate compared to the
actual rate at the sandface, complicating well test interpretations 
{cite:p}`testwells_storage`
- **Well losses:** long-term water-level declines caused by sustained groundwater
pumping {cite:p}`usgs_groundwater_depletion`.
- **Recharge:** Groundwater recharge is a critical process that replenishes aquifers,
ensuring the sustainability of water resources essential for agriculture,
drinking, and ecosystem health. {cite:p}`john2024recharge`
- **Leakage:** Groundwater seepage happens when water from the soil rises into
the foundation or lower parts of your home through capillary action 
{cite:p}`manjrekar_groundwater_seepage`
- **Boundary:** refers to the physical or hydraulic limits that define how
groundwater interacts with its surroundings, such as rivers, lakes, or
impermeable layers {cite:p}`woessner2020_boundary`
- **Positive Elapsed Time:**

## Established Project Assumptions

- A confined aquifer of effectively infinite areal extent.
- Homogeneous, isotropic aquifer properties with constant transmissivity and storativity.
- A fully penetrating pumping well with constant discharge.
- Horizontal radial flow governed by the idealized Theis formulation.
- Negligible wellbore storage, well losses, recharge, leakage, and boundary effects.
- Drawdown evaluated at positive radial distances and positive elapsed times.

## Fundamentals of Groundwater Flow
