import pytest
import numpy as np
import sys 
sys.path.insert(0, './src')
from generate_timesteps import generate_timesteps


def test_generate_mesh():
    simulation_length = 10
    num_steps = 11
    expected = np.array([0., 1., 2., 3., 4., 5., 6., 7., 8., 9., 10.])
    assert np.all(expected == generate_timesteps(simulation_length, num_steps))


def test_generate_mesh_2():
    simulation_length = 15.7
    num_steps = 20
    expected = np.zeros(num_steps - 1)
    for i in range(len(expected) - 1):
        expected[i] = simulation_length/(num_steps - 1)*i
    assert pytest.approx(expected == generate_timesteps(simulation_length, num_steps))

