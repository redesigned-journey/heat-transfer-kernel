import numpy as np
import sys


def generate_mesh(material_props, nodes_per_layer):
    """ This function generates an array of grid points in the radial direction,
    or mesh.
    Grid points are spaced evenly between the previous outer radii
    (zero for the first layer) and the specified outer radii.
    inputs
    ------
    - material_props : nested dictionary containing materials, their position
     in the particle, their radii, as well as their material properties
    - nodes_per_layer : list with the number of grid points corresponding to
    each layer

    outputs
    -------
    - mesh : a list of tuples, each tuple is composed of the material and nodes
     associated with that material
     """

    mesh = list()
    outer_radius = np.zeros(len(material_props))
    material = list()
    for key in material_props:
        for i in range(len(material_props)):
                if material_props[key]['Position'] == i:
                    outer_radius[i] = material_props[key]['Radius']
                    material.append(key)

    mesh_points = np.linspace(0, outer_radius[0], nodes_per_layer[0])
    mesh.append((material[0], mesh_points))

    for i in range(len(material_props))[1:]:
        mesh_points = np.linspace(outer_radius[i-1], outer_radius[i], nodes_per_layer[i])
        mesh.append((material[i], mesh_points))
    return mesh
