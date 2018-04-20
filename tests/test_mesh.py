import numpy as np
import pytest

from ..src.generate_mesh import generate_mesh

def test_generic():
    materials = ['Vibranium']
    expected = [('Vibranium',np.array([0, 0.5, 1]))]
    layer_outer_radii = [0, 1]
    nodes_per_layer = [3]

    mesh = generate_mesh(layer_outer_radii,nodes_per_layer, materials)
    for mat, exp in zip(mesh,expected):
        assert mat[0] == exp[0]
        assert np.allclose(mat[1], exp[1])

	
def test_several_materials():
    layer_outer_radii = [0, 1, 2, 3]
    nodes_per_layer= [3, 2, 5]
    materials = ['Vibranium', 'Unobtanium', 'Europium']
    expected = (('Vibranium',np.array([0, 0.5, 1])),('Unobtanium', np.array([1, 2])), ('Europium', np.array([2, 2.25, 2.5, 2.75, 3])))
   
    mesh = generate_mesh(layer_outer_radii,nodes_per_layer, materials)
    for mat, exp in zip(mesh,expected):
        assert mat[0] == exp[0]
        assert np.allclose(mat[1], exp[1])

