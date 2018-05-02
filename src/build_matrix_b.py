import numpy as np
from property_list_builder import property_list_builder


def build_matrix_b(boundary_conditions, mesh, material_property_library, g_dot):
    """ This function will generate the vector of constants (b) used in solving the equation A.x=b. 
	It will be relatively straightforward for the steady state case, but we are unsure how transients will affect this function.

    inputs
    ------
    - boundary conditions: the condition present at the exterior of the modeled region (interior boundary is always symmetry). 
	  This boundary condition may change with time during subsequent models.
    - mesh: the array of points for the physical location of nodes and the materials assigned to them
    - material_property_library: a dictionary or nested dictionaries of the materials used in the modeled region
    - g_dot: The internal heat generation rate of the fuel (central region)
    outputs:
    	-------
    - b: numpy array containing the matrix used in solving the equation A.x=b
    """
    k, rho, c, DR = property_list_builder(material_property_library, mesh)
  

    
    total_nodes = len(mesh[0][1])
    fuel_nodes = len(mesh[0][1])
    for i in range(1,len(mesh)):
        total_nodes += len(mesh[i][1])-1
    b = np.zeros(total_nodes)
    
    b[0:fuel_nodes-1] = g_dot/(rho[0]*c[0])
    
    #Boundary between fuel and first non-fuel material has to be handled specially
    prev_mesh_length = len(mesh[0][1])
    volume = 4/3*np.pi*((mesh[0][1][prev_mesh_length-1]+DR[0]/2)**3-(
                                                 mesh[0][1][prev_mesh_length-1]-DR[0]/2)**3)
    volume_pre_node = 4/3*np.pi*(mesh[0][1][prev_mesh_length-1]+DR[1]/2)**3
    volume_post_node = 4/3*np.pi*(mesh[0][1][prev_mesh_length-1]-DR[0]/2)**3
    
    rho_c_weighted = (volume_pre_node*rho[0]*c[0]+volume_post_node*rho[1]*c[1])/volume
        
    b[fuel_nodes] = g_dot/rho_c_weighted
    
    b[-1] = boundary_conditions

    return b

