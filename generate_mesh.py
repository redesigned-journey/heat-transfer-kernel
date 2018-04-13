import numpy as np


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
    for i in range(1, len(materials)+1):
        mesh_points = np.linspace(layer_outer_radii[i-1], layer_outer_radii[i], nodes_per_layer[i-1])
        mesh.append((materials[i-1], mesh_points)) 
        
        
        
        
        
        
    """for i in range(1, len(layer_outer_radii)):
        nodes_sum_new = nodes_sum+nodes_per_layer[i-1]
        single_material_nodes = np.linspace(layer_outer_radii[i-1],
                                            layer_outer_radii[i],
                                            nodes_per_layer[i-1])
        mesh[nodes_sum:nodes_sum_new] = single_material_nodes
        nodes_sum = nodes_sum_new"""
    return mesh
