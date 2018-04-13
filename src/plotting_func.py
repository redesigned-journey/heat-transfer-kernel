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

    plt.plot(mesh, temperature_array)
    plt.xlabel('Radial Position')
    plt.ylabel('Temperature')
    return plt.show()
