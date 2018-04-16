import numpy as np
import pytest

from generate_mesh import generate_mesh

def test_generic():
    materials = ['Vibranium']
    expected = [('Vibranium',np.array([0, 0.5, 1]))]
    layer_outer_radii = [0, 1]
    nodes_per_layer = [3]
    assert np.all([ a==b for a,b in zip(expected, generate_mesh(layer_outer_radii,nodes_per_layer, materials))])
	
	#assert np.all(expected == generate_mesh(layer_outer_radii,nodes_per_layer, materials))
	
def test_several_materials():
   layer_outer_radii = [0, 1, 2, 3]
   nodes_per_layer= [3, 2, 5]
   materials = ['Vibranium', 'Unobtanium', 'Europium']
   expected = (('Vibranium',np.array([0, 0.5, 1])),('Unobtanium', np.array([1, 2])), ('Europium', np.array([2, 2.25, 2.5, 2.75, 3])))
   assert np.all(expected == generate_mesh(layer_outer_radii,nodes_per_layer, materials))