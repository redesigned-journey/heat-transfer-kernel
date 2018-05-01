import argparse

import material_properties

import generate_mesh

# Allow for user input for material information and layers per node

parser = argparse.ArgumentParser()

parser.add_argument("-f", "--fuel", type=str, default='UO2', required=False,
	               choices=material_properties.fuel_props_master.keys(),
	               help="Determine the type of fuel used in the particle")

parser.add_argument("-c", "--clad", nargs='+', default=['Inner Pyrolytic Carbon', 'Silicon Carbide'] ,
	                choices=material_properties.cladding_props_master.keys(),
	                required=False, help="Determine the cladding materials, enter each material in quotes")

parser.add_argument("-rf", "--fuel_radius", type=float, default = 250E-6, required=False,
	                help="Determine the fuel radius")

parser.add_argument("-ct", "--clad_radii", nargs='+', default = [280E-06 , 315E-06],
	                help='Determines the cladding radii')

parser.add_argument("-ln", "--layers_per_node", nargs='+', default=[5,4,3],
	                help='Determines the layers_per_node')



    
args = parser.parse_args()
    
layers_per_node=args.layers_per_node

# Generate nested dictionary containing the materials, their radii, and their position in the particle

material_info={}
material_info[args.fuel]={'Radius' : args.fuel_radius, 'Position' : 0}

for i in range(len(args.clad)):
    material_info[args.clad[i]]={'Radius' : args.clad_radii[i], 'Position' : i+1}


material_props = material_properties.material_property_library(material_info)



mesh = generate_mesh.generate_mesh(material_props,layers_per_node)








