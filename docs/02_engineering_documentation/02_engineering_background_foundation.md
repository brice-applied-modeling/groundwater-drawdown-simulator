# Groundwater Drawdown Engineering Background

The purpose of this document, is to research, understand, and document the
engineering for the problem statement of this project.  Artificial Intelligence (AI)
was only used to help polish, but was not used to produce any of the project
understanding.

## Problem statement

Groundwater withdrawals from a pumping well lower hydraulic head in the surrounding aquifer. The resulting **drawdown** varies with pumping duration, distance from the well, and aquifer hydraulic properties. Understanding this response is fundamental to assessing well interference, monitoring-well response, and the limitations of simplified groundwater models.

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
- **Transmissivity:** The capacity of the aquifer to transmit water(Woessner & Poeter, 2020)
- **Storativity:** The capacity of an aquifer to store or release water. The 
storativity of a confined aquifer remains saturated and unchanged when there is
a unit change in the potentiometric surface (Woessner & Poeter, 2020).
- **Radial Distance:** 
- **Confined Aquifer:**
- **Homogeneous:**
- **Isotropic:**
- **Wellbore Storage:**
- **Well losses:**
- **Recharge:**
- **Leakage:**
- **Boundary:**
- **Positive Elapsed Time:**

## Established Project Assumptions

- A confined aquifer of effectively infinite areal extent.
- Homogeneous, isotropic aquifer properties with constant transmissivity and storativity.
- A fully penetrating pumping well with constant discharge.
- Horizontal radial flow governed by the idealized Theis formulation.
- Negligible wellbore storage, well losses, recharge, leakage, and boundary effects.
- Drawdown evaluated at positive radial distances and positive elapsed times.



## References

Woessner, W. W., & Poeter, E. P. (2020).
*Hydrogeologic Properties of Earth Materials and Principles
of Groundwater Flow*. The Groundwater Project.

**Section 6.4:** Properties of Aquifers and Confining Units.

[View Online](https://books.gw-project.org/hydrogeologic-properties-of-earth-materials-and-principles-of-groundwater-flow/chapter/properties-of-aquifers-and-confining-units/)
