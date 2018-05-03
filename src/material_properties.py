fuel_props_master = {'UO2':{'rho':10.5, 'k':2.5, 'c':332}}

cladding_props_master = {'Porous Carbon Buffer':{'rho':1.00, 'k':0.5, 'c':1.5},
                'Inner Pyrolytic Carbon':{'rho':1.90, 'k': 4.0, 'c': 1.5},
                'Silicon Carbide':{'rho':3.20, 'k': 13.9, 'c': 0.5},
                'Pyrolytic Carbon':{'rho':1.90, 'k': 4.0, 'c': 1.5}
                }
                




def material_property_library(material_info):
    """This function takes the materials specified in the main program
    and assigns each material their material properties.
    inputs
    ------
    material_info: Nested dictionary containing each material and their
    associated radii and position in the particle.
    outputs
    -------
    material_properties: Nested dictionary which contains the material properties for
    each material as well as their radii and position in the particle
    """


    material_props_master = {}
    material_props_master.update(fuel_props_master)
    material_props_master.update(cladding_props_master)

    for key in material_info:
        material_info[key].update(material_props_master[key])

    return material_info
