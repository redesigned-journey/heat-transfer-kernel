def boundary_conditions(layer_outer_radii, boundary_temp):
    """ This function defines the temperature on the outer radius of the particle

    Inputs
    --------
    -layer_outer_radii: calls on layer_outer_radii for the last point

    -boundary_temp: User input of the temperature at the outer radius [K]

    Outputs
    --------
    -boundary_condition: list of outer radius and temperature
    """

    temperature = 1800 "Room Temperature"

    particle_outer_radius = layer_outer_radii[-1]

    boundary_condition = [particle_outer_radius, temperature]

    return boundary_condition
