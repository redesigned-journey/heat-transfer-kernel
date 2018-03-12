# THETA - Triso HEat TrAnsfer

This project aims to build a simple heat transfer model of TRISO fuel. The goal is to provide a simple 1-D radial model of the spherical TRISO particles. Both the small fuel particles, as well as the larger scale TRISO fuel pebbles will be examined with the project.   

A numerical finite-difference approach is to be used for modeling heat transfer within the region of interest. Boundary conditions, material properties, heat generation rates, and other similar parameters will be based on data from established TRISO reactors. 

The program will produce a simple plot of the temperatures and fluxes within the fuel. Interactions with external material (such as coolant) will only be considered so far as they affect boundary conditions on the region of interest. Boundary conditions at the large pebble scale will be convective heat transfer to the coolant, or to the air in the event of coolant loss. Boundary conditions at the particle scale aren't quite as simple, and further evaluation is needed to determine what boundary condition would be appropriate.

This project will aim to remain relatively simple in terms of modeling complexity. Only spherical geometries of concentric spheres (as in the fuel particles) will be modeled, though with varying thicknesses defined by the user. Transient analysis will focus on common transients such as reactor start up, shutdown, coolant loss or loss of forced convection. Transient analysis will only go so far as determining temperature and flux variations during the transient, and will not be able to account for damage to the fuel element as a result of temperature changes.

Initially material properties will be considered constant with respect to position and temperature, with the intent to allow expansion to temperature dependent properties further along in the project. Heat generation at the particle scale will be uniform within the fueled region. At the pebble scale heat generation will be considered homogenous throughout the pebble. 

