import argparse

import material_properties

import generate_mesh

# Allow for user input for number of materials and what kind of materials

parser = argparse.ArgumentParser()
    
parser.add_argument("-n", "--number_materials", type=int, default=3, required=False,
                           help="Determines how many materials are in the particle")


parser.add_argument("-f", "--fuel", type=list(tuple), default=[('UO2',250e-6)], required=False,
	               choices=[('UO2',250e-6),('UF4',250e-6)],
	               help="Determine the type of fuel used in the particle and its radius")

parser.add_argument("-c", "--clad", type=list(tuple), default=[('Inner Pyrolytic Carbon', 35e-6) , ('Silicon Carbide', 35e-6)],
	                required=False, help="Determine the cladding materials and their thickness. List starts closest to fuel ")



    
args = parser.parse_args()
    
num_materials = args.number_materials
fuel_type = args.fuel
order_materials = (fuel_type[0]0)

cladding_list=args.clad

order_materials = [fuel_type[0][0]]
for i in range(len(cladding_list)):
    order_materials += [cladding_list[i][0]]

assert len(cladding_list) == num_materials - 1, "The number of cladding materials specified does not match number of materials in particle"


# Generate the material property library

material_props = material_properties.material_property_library(fuel_type,cladding_list)

generate_mesh.generate_mesh()



