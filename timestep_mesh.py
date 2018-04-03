import numpy as np

def generate_timesteps(simulation_length, time_step) 
"""This function generates a list of timesteps. Step points are spaced evenly between the
time 0 and the final time simulation_length in steps of time_step 

inputs 
-simulation_time: length of simulation in seconds 
-time_step: timestep in seconds 

outputs 
-time: a list of times 
""" 
 
time = np.arange(0, simulation_length, time_step)
 
return time

