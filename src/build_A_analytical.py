import numpy as np

def build_A_analytical(material_property_library, mesh, materials):
    """ While not intended for long term use, 
	    this function demonstrates that our steady state model matches
		the analytical solution.
		inputs:
		material_property_library contains relevant material data
		mesh contains the radial positions of the nodes
		
		outputs:
		T is the array of temperatures at each node.
    """

    k = material_property_library[materials[0][0]]['k']
    rho = material_property_library[materials[0][0]]['rho']
    c = material_property_library[materials[0][0]]['c']
    N=len(mesh)
    r_outer=mesh[N-1]
    g = 1.1*10**10
    C2 = 800+g*r_outer**2/(6*k)
    
    T = np.zeros(len(mesh))
    for i in range(0, len(mesh)):
        T[i] = C2-g*mesh[i]**2/(6*k)
    
    return T