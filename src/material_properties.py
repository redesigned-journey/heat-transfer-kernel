def material_property_library(fuel_type, cladding_list):
    material_props_master = {
                'UO2':{'rho':10.5, 'k':2.5, 'c':332},
                'Porous Carbon Buffer':{'rho':1.00, 'k':0.5, 'c':1.5},
                'Innner Pyrolytic Carbon':{'rho':1.90, 'k': 4.0, 'c': 1.5},
                'Silicon Carbide':{'rho':3.20, 'k': 13.9, 'c': 0.5},
                'Pyrolytic Carbon':{'rho':1.90, 'k': 4.0, 'c': 1.5}
                }

    material_props = {}
    material_props[fuel_type[0][0]] = material_props_master[fuel_type[0][0]]
    material_props[fuel_type[0][0]]['layer_thickness'] = fuel_type[0][1]

    for i in range(len(cladding_list)):
        material_props[cladding_list[i][0]]=material_props_master[cladding_list[i][0]]
        material_props[cladding_list[i][0]]['layer_thickness']=(cladding_list[i][1])


    return material_props