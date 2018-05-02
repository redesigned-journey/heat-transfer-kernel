import numpy as np
import sys
from property_list_builder import property_list_builder


def build_matrix_A(material_property_library, mesh):
    """ This function will take a previously generated mesh and create the 'A'
    matrix used in solving this problem.

    inputs:
    --------
    - material_property_library: this will be a dictionary or nested dictionary
    containing all of the important data for each material (fuel,
    various layers of graphite)
    - mesh: the physical location of each mesh point
    - time: An array of timesteps taken during transients. If steady state, supply 0.
    --------
    - An array that can be plugged into a subsequent function to solve the
      A.x=b formula
    """
   

    
    k, rho, c, DR = property_list_builder(material_property_library, mesh)
    
    total_nodes = len(mesh[0][1])
    for i in range(1, len(mesh)):
        total_nodes += len(mesh[i][1])-1
        
    A = np.zeros((total_nodes, total_nodes))
    volume = np.zeros(total_nodes)
    
    "Begin by setting boundary nodes"
    "Have to treat nodes 0 and 1 differently to avoid divide by zero"
    volume = 4/3*np.pi*(mesh[0][1][0]+DR[0]/2)**3
    
    
    A[0, 0] = k[0]*4*np.pi/(rho[0]*c[0])/(DR[0]*volume)*(DR[0]/2)**2
    A[0, 1] = -A[0,0]
	

    volume = 4/3*np.pi*(mesh[0][1][1]+DR[0]/2)**3-(mesh[0][1][1]-DR[0]/2)**3
    
    A[1, 0] = -k[0]*4*np.pi/(rho[0]*c[0])/(DR[0]*volume)*(mesh[0][1][0]+DR[0]/2)**2
    A[1, 2] = -k[0]*4*np.pi/(rho[0]*c[0])/volume*(1/(1/mesh[0][1][1]-1/mesh[0][1][2]))
    A[1, 1] = -(A[1,0] +A[1,2])

	
    for i in range(2, len(mesh[0][1])-1): #Length set to fueled node length
        volume = 4/3*np.pi*((mesh[0][1][i]+DR[0]/2)**3-(mesh[0][1][i]-DR[0]/2)**3)
        A[i, i] = k[0]*4*np.pi/(rho[0]*c[0])/volume*(1/(1/mesh[0][1][i]-1/mesh[0][1][i+1]) +
                                        1/(1/mesh[0][1][i-1]-1/mesh[0][1][i]))
        A[i, i-1] = -k[0]*4*np.pi/(rho[0]*c[0])/volume*(1/(1/mesh[0][1][i-1]-1/mesh[0][1][i]))
        A[i, i+1] = -k[0]*4*np.pi/(rho[0]*c[0])/volume*(1/(1/mesh[0][1][i]-1/mesh[0][1][i+1]))
		
    #Now need to handle the boundary nodes
    #i is currently the value of the node at the internal boundary
    for mat in range(1, len(mesh)):
        prev_mesh_length = len(mesh[mat-1][1])
        volume = 4/3*np.pi*((mesh[mat-1][1][prev_mesh_length-1]+DR[mat]/2)**3-(
                                                 mesh[mat-1][1][prev_mesh_length-1]-DR[mat-1]/2)**3)
        volume_pre_node = 4/3*np.pi*(mesh[mat-1][1][prev_mesh_length-1]+DR[mat]/2)**3
        volume_post_node = 4/3*np.pi*(mesh[mat-1][1][prev_mesh_length-1]-DR[mat-1]/2)**3
        
        #This line will create a weighted value of rho c for the boundary node
        rho_c_weighted = (volume_pre_node*rho[mat-1]*c[mat-1]+volume_post_node*rho[mat]*c[mat])/volume
        
        A[i+1,i+2] = -k[mat]*4*np.pi/(rho_c_weighted)/volume*(1/(1/mesh[mat][1][0]-1/mesh[mat][1][1]))
        A[i+1,i+1] = (k[mat-1]*4*np.pi/(rho_c_weighted)/volume*(1/(1/mesh[mat-1][1][prev_mesh_length-2]
                                                    -1/mesh[mat-1][1][prev_mesh_length-1]))+(
                                                    k[mat]*4*np.pi/(rho_c_weighted)/volume*(1/(1/mesh[mat][1][0]
                                                    -1/mesh[mat][1][1]))))
        A[i+1, i] = -k[mat-1]*Dt*4*np.pi/(rho_c_weighted)/volume*(1/(1/mesh[mat-1][1][prev_mesh_length-2]-
                                                                        1/mesh[mat-1][1][prev_mesh_length-1]))
	
        for j in range(1, len(mesh[mat][1])-1): 
            volume = 4/3*np.pi*((mesh[mat][1][j]+DR[mat]/2)**3-(mesh[mat][1][j]-DR[mat]/2)**3)
            A[j+i+1, j+i+1] = k[mat]*4*np.pi/(rho[mat]*c[mat])/volume*(1/(1/mesh[mat][1][j]-1/mesh[mat][1][j+1]) +
                                        1/(1/mesh[mat][1][j-1]-1/mesh[mat][1][j]))
            A[j+i+1, j-1+i+1] = -k[mat]*4*np.pi/(rho[mat]*c[mat])/volume*(1/(1/mesh[mat][1][j-1]-1/mesh[mat][1][j]))
            A[j+i+1, j+1+i+1] = -k[mat]*4*np.pi/(rho[mat]*c[mat])/volume*(1/(1/mesh[mat][1][j]-1/mesh[mat][1][j+1]))
        i+=len(mesh[mat][1])-1

    A[total_nodes-1, total_nodes-1] = 1


    return A


