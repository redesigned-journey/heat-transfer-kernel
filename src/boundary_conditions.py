def boundary_conditions(particle_outer_radius, boundary_temp):
    """ This function defines the temperature on the outer radius of the particle

    Inputs
    --------
    -particle_outer_radius: Outer radius of particle

    -boundary_temp: User input of the temperature at the outer radius [K]

    Outputs
    --------
    -boundary_condition: list of outer radius and temperature
    """

    boundary_condition = [particle_outer_radius, boundary_temp]

    return boundary_condition

