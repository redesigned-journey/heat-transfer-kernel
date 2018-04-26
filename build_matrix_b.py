import numpy as np


def build_matrix_b(boundary_conditions, mesh, material_property_library, g_dot, time):
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
    k = np.zeros(len(mesh))
    rho = np.zeros(len(mesh))
    c = np.zeros(len(mesh))
    for m in range(len(mesh)):
        k[m] += material_property_library[mesh[m][0]]['k']
        rho[m] += material_property_library[mesh[m][0]]['rho']
        c[m] += material_property_library[mesh[m][0]]['c']
    Dt = time[1]-time[0]

    
    total_nodes = len(mesh[0][1])
    for i in range(1,len(mesh)):
        total_nodes += len(mesh[i][1])-1
    b = np.zeros(total_nodes)
    for i in range(len(mesh[0][1])):
        b[i] = -g_dot*Dt/(rho[0]*c[0])
    b[total_nodes-1] = boundary_conditions

    return b

