import numpy as np


def build_matrix_b(boundary_conditions,mesh,material_property_library,materials):
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
	
    k = material_property_library[materials[0][0]]['k']
    rho = material_property_library[materials[0][0]]['rho']
    c = material_property_library[materials[0][0]]['c']
    g_dot = 1.1*10**10
    "g_dot should probably be passed into the function so it can be varied with time" 
    

    N = len(mesh)
    b = np.zeros(N)
    
    b[N-1] = boundary_conditions
    for i in range(0,N-1):
        b[i] = -g_dot

    return b

