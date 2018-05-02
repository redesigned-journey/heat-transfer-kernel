import numpy as np

def property_list_builder(material_property_library, mesh):
    """Builds the lists of rho, c, k, and DR for the materials in the model
    inputs: 
    - material_property_library: this will be a dictionary or nested dictionary
    containing all of the important data for each material (fuel,
    various layers of graphite)
    - mesh: the physical location of each mesh point
    
    output:
    -k, rho, c, DR = lists of material properties for each material
    """
    k = np.zeros(len(mesh))
    rho = np.zeros(len(mesh))
    c = np.zeros(len(mesh))
    DR = np.zeros(len(mesh))
    for m in range(len(mesh)):
        mat_name = mesh[m][0]
        k[m] = material_property_library[mat_name]['k']
        rho[m] = material_property_library[mat_name]['rho']
        c[m] = material_property_library[mat_name]['c']
        DR[m] = mesh[m][1][1]-mesh[m][1][0]

    return k, rho, c, DR