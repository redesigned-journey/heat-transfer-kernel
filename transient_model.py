import numpy as np
from build_matrix_A import build_matrix_A
from build_matrix_b import build_matrix_b
from matrix_solver import solve_matrix
from generate_mesh import generate_mesh

def transient_model(time, material_property_library, mesh, g_dot_list, boundary_conditions_list):
    """This function will calculate the transient response of the fuel particle to changes in either heat
    generation rate or to boundary wall temperature. The A matrix has 1 added to its diagonal entries while
    the b matrix has the previous temperature set added to its entries. These changes need to be made now that 
    dT/dt is no longer zero:
    
    T_time+1 = T_time + dT/dt *Delta_t
    
    Where previously dT/dt was equal to zero, the matrices simplified dramatically. Now this is not the case,
    so the b matrix must be appended with the known constant T_time and the A matrix must be appended with 1 
    along the diagonal to account for the presence of T_time+1.
       
    inputs
    ------
    - time: An array of the time steps taken by the solver. Passed through to the matrix generators.
    - mesh: the array of points for the physical location of nodes and the materials assigned to them
    - material_property_library: a dictionary or nested dictionaries of the materials used in the modeled region
    - g_dot_list: a list with the heat generation rates before the transient and during the transient. g_dot_list 
    is of length 2, with the 0th entry being prior to the transient and fist entry after time zero.
    - boundary_condtions_list: a list with the boundary temperature before the transient and during the transient
    outputs. This list is of length 2, with the 0th entry being prior to the transient and fist entry after time zero.
    -T: numpy array containing the temperatures for each node and time
    """  
    
    total_nodes = len(mesh[0][1])
    for i in range(1,len(mesh)):
        total_nodes += len(mesh[i][1])-1
    T = np.zeros((total_nodes, len(time)))
    
    A = build_matrix_A(material_property_library, mesh, time)
    b = build_matrix_b(boundary_conditions_list[0], mesh, material_property_library, g_dot_list[0], time) 
    
    T_initial = solve_matrix(A,b)
    
    A += np.eye(A.shape[0])
    #The following line removes the addition of one from the final entry, where the boundary condition is imposed.
    A[-1,-1] += -1
    
    b = np.add(T_initial,b)
    b[-1] += -T_initial[-1]

    T[:,0] = T_initial

    
    b_temp = build_matrix_b(boundary_conditions_list[1], mesh, material_property_library, g_dot_list[1], time)    
    
    for i in range(1,len(time)):
        b = b_temp.copy() 
        b += np.add(b, T[:,i-1])
        #The following line removes the addition 
        b[-1] += -T[-1,i-1]
        
        T[:,i] = solve_matrix(A, b)
    
    return T
    