import matplotlib.pyplot as plt


def temperature_plot(temperature_array, mesh):

    """ This function will generate a plot of the temperatures at each node.

    inputs
    -------
    temperature_array: This is an array containing temperatures at each node
    mesh: An array containing the radial position for each

    outputs
    -------
    A lovely plot of the temperature distribution.
    """
    
    mesh_radii = []
    for element in mesh:
        for node in element[1]:
            mesh_radii += [node]
    
    mesh_radii_set = list(set(mesh_radii))
    mesh_radii_ordered = sorted(mesh_radii_set, key=float)     
    
    plt.plot(mesh_radii_ordered, temperature_array)
    plt.xlabel('Radial Position (m)')
    plt.ylabel('Temperature (K)')
    return plt.show()
