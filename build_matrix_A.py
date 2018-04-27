import numpy as np


def build_matrix_A(material_property_library, mesh, time):
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
    k = np.zeros(len(mesh))
    rho = np.zeros(len(mesh))
    c = np.zeros(len(mesh))
    DR = np.zeros(len(mesh))
    if len(time) > 1:
    	Dt = time[1] - time[0]
    else:
    	Dt = 1
    for m in range(len(mesh)):
        k[m] = material_property_library[mesh[m][0]]['k']
        rho[m] = material_property_library[mesh[m][0]]['rho']
        c[m] = material_property_library[mesh[m][0]]['c']
        DR[m] = mesh[m][1][1]-mesh[m][1][0]


    total_nodes = len(mesh[0][1])
    for i in range(1, len(mesh)):
        total_nodes += len(mesh[i][1])-1
        
    A = np.zeros((total_nodes, total_nodes))
    volume = np.zeros(total_nodes)
    
    "Begin by setting boundary nodes"
    "Have to treat nodes 0 and 1 differently to avoid divide by zero"
    volume[0] = 4/3*np.pi*(mesh[0][1][0]+DR[0]/2)**3
    volume[1] = 4/3*np.pi*(mesh[0][1][1]+DR[0]/2)**3-(mesh[0][1][1]-DR[0]/2)**3
    
    A[0, 0] = k[0]*Dt*4*np.pi/(rho[0]*c[0])/(DR[0]*volume[0])*(DR[0]/2)**2
    A[0, 1] = -k[0]*Dt*4*np.pi/(rho[0]*c[0])/(DR[0]*volume[0])*(DR[0]/2)**2
	

    A[1, 1] = k[0]*Dt*4*np.pi/(rho[0]*c[0])/volume[1]*(1/(1/mesh[0][1][1]-1/mesh[0][1][2]) +
                                    1/DR[0]*(mesh[0][1][0]+DR[0]/2)**2)
    A[1, 0] = -k[0]*Dt*4*np.pi/(rho[0]*c[0])/(DR[0]*volume[1])*(mesh[0][1][0]+DR[0]/2)**2
    A[1, 2] = -k[0]*Dt*4*np.pi/(rho[0]*c[0])/volume[1]*(1/(1/mesh[0][1][1]-1/mesh[0][1][2]))
	

	
    for i in range(2, len(mesh[0][1])-1): #Length set to fueled node length
        volume[i] = 4/3*np.pi*((mesh[0][1][i]+DR[0]/2)**3-(mesh[0][1][i]-DR[0]/2)**3)
        A[i, i] = k[0]*Dt*4*np.pi/(rho[0]*c[0])/volume[i]*(1/(1/mesh[0][1][i]-1/mesh[0][1][i+1]) +
                                        1/(1/mesh[0][1][i-1]-1/mesh[0][1][i]))
        A[i, i-1] = -k[0]*Dt*4*np.pi/(rho[0]*c[0])/volume[i]*(1/(1/mesh[0][1][i-1]-1/mesh[0][1][i]))
        A[i, i+1] = -k[0]*Dt*4*np.pi/(rho[0]*c[0])/volume[i]*(1/(1/mesh[0][1][i]-1/mesh[0][1][i+1]))
		
    #Now need to handle the boundary nodes
    #i is currently the value of the node at the internal boundary
    for mat in range(1, len(mesh)):
        prev_mesh_length = len(mesh[mat-1][1])
        volume[i+1] = 4/3*np.pi*((mesh[mat-1][1][prev_mesh_length-1]+DR[mat]/2)**3-(
                                                 mesh[mat-1][1][prev_mesh_length-1]-DR[mat-1]/2)**3)
        A[i+1,i+2] = -k[mat]*Dt*4*np.pi/(rho[mat-1]*c[mat-1])/volume[i+1]*(1/(1/mesh[mat][1][0]-1/mesh[mat][1][1]))
        A[i+1,i+1] = (k[mat-1]*Dt*4*np.pi/(rho[mat-1]*c[mat-1])/volume[i+1]*(1/(1/mesh[mat-1][1][prev_mesh_length-2]
                                                    -1/mesh[mat-1][1][prev_mesh_length-1]))+(
                                                    k[mat]*Dt*4*np.pi/(rho[mat-1]*c[mat-1])/volume[i+1]*(1/(1/mesh[mat][1][0]
                                                    -1/mesh[mat][1][1]))))
        A[i+1, i] = -k[mat-1]*Dt*4*np.pi/(rho[mat-1]*c[mat-1])/volume[i+1]*(1/(1/mesh[mat-1][1][prev_mesh_length-2]-
                                                                        1/mesh[mat-1][1][prev_mesh_length-1]))
	
        for j in range(1, len(mesh[mat][1])-1): 
            volume[j+i+1] = 4/3*np.pi*((mesh[mat][1][j]+DR[mat]/2)**3-(mesh[mat][1][j]-DR[mat]/2)**3)
            A[j+i+1, j+i+1] = k[mat]*Dt*4*np.pi/(rho[mat]*c[mat])/volume[j+i+1]*(1/(1/mesh[mat][1][j]-1/mesh[mat][1][j+1]) +
                                        1/(1/mesh[mat][1][j-1]-1/mesh[mat][1][j]))
            A[j+i+1, j-1+i+1] = -k[mat]*Dt*4*np.pi/(rho[mat]*c[mat])/volume[j+i+1]*(1/(1/mesh[mat][1][j-1]-1/mesh[mat][1][j]))
            A[j+i+1, j+1+i+1] = -k[mat]*Dt*4*np.pi/(rho[mat]*c[mat])/volume[j+i+1]*(1/(1/mesh[mat][1][j]-1/mesh[mat][1][j+1]))
        i+=j+1

    A[total_nodes-1, total_nodes-1] = 1


    return A
