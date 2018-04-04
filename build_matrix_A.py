import numpy as np


def build_matrix_A(material_property_library, mesh):
    """ This function will take a previously generated mesh and create the 'A'
    matrix used in solving this problem.

    inputs:
    --------
    - material_property_library: this will be a dictionary or nested dictionary
    containing all of the important data for each material (fuel,
    various layers of graphite)
    - mesh: the physical location of each mesh point and the material assigned
    to each mesh point

    outputs
    --------
    - An array that can be plugged into a subsequent function to solve the
    A.x=b formula
    """

    k = material_property_library['k']
    rho = material_property_library['rho']
    c = material_property_library['c']

    N = len(mesh)
    A = np.zeros((N, N))
    volume = np.zeros(N)
    DR = mesh[1]-mesh[0]
    "Begin by setting boundary nodes"
    "Have to treat nodes 0 and 1 differently to avoid divide by zero"
    volume[0] = 4/3*np.pi*(mesh[0]+DR/2)**3
    volume[1] = 4/3*np.pi*(mesh[1]+DR/2)**3-(mesh[1]-DR/2)**3
    A[N-1, N-1] = 1
    A[0, 0] = -k*4*np.pi/(DR*volume[0])*(mesh[0]+DR/2)**2
    A[0, 1] = k*4*np.pi/(DR*volume[0])*(mesh[0]+DR/2)**2

    A[1, 1] = -k*4*np.pi/volume[1]*(1/(1/mesh[1]-1/mesh[2]) +
                                    1/DR*(mesh[0]+DR/2)**2)
    A[1, 0] = k*4*np.pi/(DR*volume[1])*(mesh[0]+DR/2)**2
    A[1, 2] = k*4*np.pi/volume[1]*(1/(1/mesh[1]-1/mesh[2]))

    for i in range(2, N-1):
        volume[i] = 4/3*np.pi*((mesh[i]+DR/2)**3-(mesh[i]-DR/2)**3)
        A[i, i] = -k*4*np.pi/volume[i]*(1/(1/mesh[i]-1/mesh[i+1]) +
                                        1/(1/mesh[i-1]-1/mesh[i]))
        A[i, i-1] = k*4*np.pi/volume[i]*(1/(1/mesh[i-1]-1/mesh[i]))
        A[i, i+1] = k*4*np.pi/volume[i]*(1/(1/mesh[i]-1/mesh[i+1]))
    return A
