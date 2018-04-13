import numpy as np
import pytest

from generate_mesh import generate_mesh

def test_generic():
	expected = np.array([0, 0.5, 1])
	layer_outer_radii = [0, 1]
	nodes_per_layer = [3]
	
	assert np.all(expected == generate_mesh(layer_outer_radii,nodes_per_layer))
	
def test_several_materials():
   layer_outer_radii = [0, 1, 2, 3]
   nodes_per_layer= [3, 2, 5]
   expected = np.array([0, 0.5, 1, 1, 2, 2, 2.25, 2.5, 2.75, 3])
   assert np.all(expected == generate_mesh(layer_outer_radii,nodes_per_layer))