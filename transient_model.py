import numpy as np
from build_matrix_A import build_matrix_A
from build_matrix_b import build_matrix_b
from matrix_solver import solve_matrix
from build_A_analytical import build_A_analytical
from generate_mesh import generate_mesh

def transient_model(time, material_property_library, mesh, g_dot_list, boundary_conditions_list):
    "Will also have to pass in however bcs or heat generation rate change with time"
    "Begin by setting up the initial conditions"
    """This function will calculate the transient response of the fuel particle to changes in either heat
    generation rate or to boundary wall temperature. The A matrix has 1 added to its diagonal entries while
    the b matrix has the previous temperature set added to its entries.
       
    inputs
    ------
    - time: An array of the time steps taken by the solver. Passed through to the matrix generators.
    - mesh: the array of points for the physical location of nodes and the materials assigned to them
    - material_property_library: a dictionary or nested dictionaries of the materials used in the modeled region
    - g_dot_vec: a list with the heat generation rates before the transient and during the transient
    - boundary_condtions_list: a list with the boundary temperature before the transient and during the transient
    outputs
    -T: numpy array containing the temperatures for each node and time
    """    
    total_nodes = len(mesh[0][1])
    for i in range(1,len(mesh)):
        total_nodes += len(mesh[i][1])-1
    T = np.zeros((total_nodes, len(time)))
    
    A = build_matrix_A(material_property_library, mesh, time)
    b = build_matrix_b(boundary_conditions_list[0], mesh, material_property_library, g_dot_list[0], time) 
    
    T_initial = solve_matrix(A,b)
    
    for j in range((A.shape[0])-1):
        A[j,j] += 1
        b[j] += T_initial[j] 
    T[:,0] = solve_matrix(A,b)
    
    for i in range(1,len(time)):
        b = build_matrix_b(boundary_conditions_list[1], mesh, material_property_library, g_dot_list[1], time)
        for k in range(len(b)-1):
            b[k] += T[k,i-1]
        
        T[:,i] = solve_matrix(A, b)
    
    return T