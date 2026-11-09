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
- **Confined Aquifer:** The aquifer is bounded above and below by low hydraulic
conductivity layers, known as aquitards.  Aquitards can still transmit seepage,
but it is generally low. {cite:p}`theis1935`.
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
- **Wellbore Storage:** Wellbore storage describes the temporary contribution
of water stored within a well to the water being pumped, particularly during
the early stages of pumping.

When pumping begins, some of the discharged water initially comes from storage
within the well itself rather than entirely from the surrounding aquifer.

As pumping continues, the contribution from aquifer flow generally becomes more
dominant.
- **Groundwater Depletion:** long-term water-level declines caused by sustained
groundwater pumping {cite:p}`usgs_groundwater_depletion`.
- **Recharge:** Groundwater recharge is a critical process that replenishes
aquifers, ensuring the sustainability of water resources essential for agriculture,
drinking, and ecosystem health. {cite:p}`barlow2012`
- **Leakage:** Leakage in a confined aquifer is water moving vertically through
the confining layer above or below it, usually because the water pressure
(hydraulic head) differs between the aquifer and a neighboring layer.

The confining layer, often called an aquitard, is not perfectly impermeable, so
water can slowly seep through it. Pumping can lower the aquifer’s water level
and increase this seepage; water may leak into the aquifer from above or below,
or out of it, depending on the head difference. Theis’s original equation assumes
no such leakage; leaky-aquifer analyses use modified methods such as Hantush’s.
{cite:p}`hydrosolve_theis`
- **Boundary:** refers to the physical or hydraulic limits that define how
groundwater interacts with its surroundings, such as rivers, lakes, or
impermeable layers {cite:p}`woessner2020_boundary`
- **Groundwater Age:** The age of groundwater refers to the time that has
elapsed since a water particle entered the saturated zone as groundwater recharge.
This concept is important for understanding the mean residence time, which
indicates how long water remains in an aquifer before it is discharged.
{cite:p}`cook2020`
- **Well Losses:** In groundwater hydraulics, well losses refer to the
additional hydraulic head losses associated with groundwater entering and
moving through a pumping well.

## Established Project Assumptions

- A confined aquifer of effectively infinite areal extent.
- Homogeneous, isotropic aquifer properties with constant transmissivity and storativity.
- A fully penetrating pumping well with constant discharge.
- Horizontal radial flow governed by the idealized Theis formulation.
- Negligible wellbore storage, well losses, recharge, leakage, and boundary effects.
- Drawdown evaluated at positive radial distances and positive elapsed times.

## Fundamentals of Groundwater Flow


