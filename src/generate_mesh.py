import numpy as np
import sys

def generate_mesh(layer_outer_radii, nodes_per_layer, materials):
    """ This function generates an array of grid points in the radial direction,
    or mesh.
    Grid points are spaced evenly between the previous outer radii
    (zero for the first layer) and the specified outer radii.
    generate_mesh returns a single array of r values

    inputs
    ------
    - layer_outer_radii : list of radii for each layer of the fuel particle.
    The first layer is assumed to start at r=0
    - nodes_per_layer : list with the number of grid points
      corresponding to each layer
    - materials : a list of the materials in the order in which they appear

    outputs
    -------
    - mesh : a list of tuples, each tuple is composed of the material and nodes associated with that material
    """
    mesh = list()
    for i in range(len(materials)):
        mesh_points = np.linspace(layer_outer_radii[i], layer_outer_radii[i+1], nodes_per_layer[i])
        mesh.append((materials[i], mesh_points))
    return mesh
