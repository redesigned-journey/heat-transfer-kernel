import materials_dict_master.py


def mat_properties(materials)
""" This will generate a nested dictionary for the materials and important material properties that will be used in other functions. Material information will be stored in an external file that is read in using this function.

inputs
materials: The materials that will be used in the particular run of the program.
outputs
material_property_library: dictionary containing the material properties for each material to be modeled.
"""

   
    material_property_library = {'materials[0]': {'rho': materials_dict_master['material[0]']['rho'], 'k': materials_dict_master['material[0]']['k'], 'c': materials_dict_master['material[0]']['c'] },
                                 'materials[1]': {'rho': materials_dict_master['material[1]']['rho'], 'k': materials_dict_master['material[1]']['k'], 'c': materials_dict_master['material[1]']['c'] },
                                 'materials[2]': {'rho': materials_dict_master['material[2]']['rho'], 'k': materials_dict_master['material[2]']['k'], 'c': materials_dict_master['material[2]']['c'] },
                                 'materials[3]': {'rho': materials_dict_master['material[3]']['rho'], 'k': materials_dict_master['material[3]']['k'], 'c': materials_dict_master['material[3]']['c'] },
                                 'materials[4]': {'rho': materials_dict_master['material[4]']['rho'], 'k': materials_dict_master['material[4]']['k'], 'c': materials_dict_master['material[4]']['c'] },
    

    return material_property_library
