import numpy as np


def build_matrix_A(material_property_library, mesh):
    """ This function will take a previously generated mesh and create the 'A'
    matrix used in solving this problem.

    inputs:
    --------
    - material_property_library: this will be a dictionary or nested dictionary
    containing all of the important data for each material (fuel,
    various layers of graphite)
    - mesh: the physical location of each mesh point
    - materials: the materials in each region and how many nodes are assigned to that material
    outputs. List of tuples of format (material, number of nodes)
    --------
    - An array that can be plugged into a subsequent function to solve the
    A.x=b formula
    """
    fuel_material = mesh[0][0]
    k = material_property_library[fuel_material]['k']
    rho = material_property_library[fuel_material]['rho']
    c = material_property_library[fuel_material]['c']

    total_nodes = len(mesh[0][1])
    for i in range(1, len(mesh)):
        total_nodes += len(mesh[i][1])-1
        
    N = len(mesh)
    A = np.zeros((total_nodes, total_nodes))
    A_test = np.zeros((3,total_nodes))
    volume = np.zeros(total_nodes)
    
    DR = mesh[0][1][1]-mesh[0][1][0]
    "Begin by setting boundary nodes"
    "Have to treat nodes 0 and 1 differently to avoid divide by zero"
    volume[0] = 4/3*np.pi*(mesh[0][1][0]+DR/2)**3
    volume[1] = 4/3*np.pi*(mesh[0][1][1]+DR/2)**3-(mesh[0][1][1]-DR/2)**3
    
    A[0, 0] = -k*4*np.pi/(DR*volume[0])*(DR/2)**2
    A[0, 1] = k*4*np.pi/(DR*volume[0])*(DR/2)**2
	

    A[1, 1] = -k*4*np.pi/volume[1]*(1/(1/mesh[0][1][1]-1/mesh[0][1][2]) +
                                    1/DR*(mesh[0][1][0]+DR/2)**2)
    A[1, 0] = k*4*np.pi/(DR*volume[1])*(mesh[0][1][0]+DR/2)**2
    A[1, 2] = k*4*np.pi/volume[1]*(1/(1/mesh[0][1][1]-1/mesh[0][1][2]))
	
    #A_test[1,0] = A[0,0]
    #A_test[2,0] = A[0,1]

	
    for i in range(2, len(mesh[0][1])-1): #Length set to fueled node length
        volume[i] = 4/3*np.pi*((mesh[0][1][i]+DR/2)**3-(mesh[0][1][i]-DR/2)**3)
        A[i, i] = -k*4*np.pi/volume[i]*(1/(1/mesh[0][1][i]-1/mesh[0][1][i+1]) +
                                        1/(1/mesh[0][1][i-1]-1/mesh[0][1][i]))
        A[i, i-1] = k*4*np.pi/volume[i]*(1/(1/mesh[0][1][i-1]-1/mesh[0][1][i]))
        A[i, i+1] = k*4*np.pi/volume[i]*(1/(1/mesh[0][1][i]-1/mesh[0][1][i+1]))
		
    #Now need to handle the boundary nodes
    #i is currently the value of the node at the internal boundary
    k2 = material_property_library[mesh[1][0]]['k']
    rho2 = material_property_library[mesh[1][0]]['rho']
    c2 = material_property_library[mesh[1][0]]['c']
    DR2 = mesh[1][1][1]-mesh[1][1][0]
    A[i+1,i+2] = k2/DR2
    A[i+1,i+1] = -k/DR-k2/DR2
    A[i+1, i] = k/DR
	
    for j in range(1, len(mesh[1][1])-1): 
        volume[j+i+1] = 4/3*np.pi*((mesh[1][1][j]+DR2/2)**3-(mesh[1][1][j]-DR2/2)**3)
        A[j+i+1, j+i+1] = -k2*4*np.pi/volume[j+i+1]*(1/(1/mesh[1][1][j]-1/mesh[1][1][j+1]) +
                                        1/(1/mesh[1][1][j-1]-1/mesh[1][1][j]))
        A[j+i+1, j-1+i+1] = k2*4*np.pi/volume[j+i+1]*(1/(1/mesh[1][1][j-1]-1/mesh[1][1][j]))
        A[j+i+1, j+1+i+1] = k2*4*np.pi/volume[j+i+1]*(1/(1/mesh[1][1][j]-1/mesh[1][1][j+1]))
    A[total_nodes-1,total_nodes-1] = 1

    """for k in range(total_nodes-1):
        A_test[0,k] = A[k, k-1]
        A_test[1,k] = A[k,k]
        A_test[2,k] = A[k,k+1]	
    A_test[1,total_nodes-1] = A[total_nodes-1, total_nodes-1] """
    return A
