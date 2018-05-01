import numpy as np
import sys


def generate_timesteps(simulation_length, num_steps):
    """This function generates a list of timesteps. Step points are spaced evenly
    between the time 0 and the final time simulation_length based on the number of
    timesteps num_steps.

    inputs
    -simulation_time: length of simulation in seconds
    -num_steps: the number of timesteps

    outputs
    -time: a list of times
    """

    time = np.linspace(0, simulation_length, num=num_steps)
    return time
