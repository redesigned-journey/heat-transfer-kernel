import numpy as np


def build_matrix_b(boundary_conditions,mesh,material_property_library):
    """ This function will generate the vector of constants (b) used in solving the equation A.x=b. 
	It will be relatively straightforward for the steady state case, but we are unsure how transients will affect this function.

    inputs
    ------
    boundary conditions: the condition present at the exterior of the modeled region (interior boundary is always symmetry). 
	This boundary condition may change with time during subsequent models.
    mesh: the array of points for the physical location of nodes and the materials assigned to them
    material_property_library: a dictionary or nested dictionaries of the materials used in the modeled region
    outputs
    numpy array containing the matrix used in solving the equation A.x=b
    """
    fuel_material = mesh[0][0]
    k = material_property_library[mesh[0][0]]['k']
    rho = material_property_library[mesh[0][0]]['rho']
    c = material_property_library[mesh[0][0]]['c']
    g_dot = 1.1*10**10
    "g_dot should probably be passed into the function so it can be varied with time" 
    
    total_nodes = len(mesh[0][1])
    for i in range(1,len(mesh)):
        total_nodes += len(mesh[i][1])-1
    b = np.zeros(total_nodes)
    #for i in range(len(mesh[0][1])):
    for i in range(total_nodes-1):
        b[i] = -g_dot
    b[total_nodes-1] = boundary_conditions

    return b

