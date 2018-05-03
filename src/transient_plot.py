import matplotlib.pyplot as plt
import numpy as np

def transient_plot(T_mat, mesh):
    """This function will plot each of the arrays from the output of the transient model at each timestep on a single 2D graph.
    
    imputs
    ------
    - T_mat: The 2D matrix from the output of the transient_model function
    - mesh: mesh: the array of points for the physical location of nodes and the materials assigned to them
    
    output
    ------
    A plot of the temperature at each node, at each timestep
    """
    
    mesh_radii = []
    counter = 0
    for element in mesh:
        for node in element[1]:
            mesh_radii += [node]
    
    mesh_radii_set = list(set(mesh_radii))
    mesh_radii_ordered = sorted(mesh_radii_set, key=float)    
           
     
    fig = plt.figure()
    fig.suptitle('Transient Model')              
    for i in range(0, len(T_mat[0,:])):
        plt.plot(mesh_radii_ordered, T_mat[:,i])
        
    plt.xlabel('Radial Position (m)')
    plt.ylabel('Temperature (K)')
    
    plt.legend()
    plt.show()
