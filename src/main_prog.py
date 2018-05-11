import argparse

import material_properties

import generate_mesh

import build_matrix_A

import build_matrix_b

import boundary_conditions

import matrix_solver

import steady_state_plot

import transient_plot

import transient_model

import generate_timesteps


# Allow for user input for material information and layers per node

parser = argparse.ArgumentParser()


parser.add_argument("-f", "--fuel", type=str, default='UO2', required=False,
                    choices=material_properties.fuel_props_master.keys(),
                    help="Determine the type of fuel used in the particle")

parser.add_argument("-c", "--clad", nargs='+',
                    default=['Inner Pyrolytic Carbon', 'Silicon Carbide'],
                    choices=material_properties.cladding_props_master.keys(),
                    required=False,
                    help="Determine the cladding materials, enter each \
                    material in quotes starting closest to fuel")

parser.add_argument("-rf", "--fuel_radius", type=float, default=250E-6,
                    required=False,
	                help="Determine the fuel radius")


parser.add_argument("-ct", "--clad_radii", nargs='+',
                    default=[280E-06, 315E-06],
                    help='Determines the cladding radii')

parser.add_argument("-ln", "--layers_per_node", nargs='+', default=[5, 4, 3],
                     help='Determines the layers_per_node')

parser.add_argument("-tr", "--transient", nargs='+', type=float, default=[],
                    required=False,
	                help="Runs transient model. Enter simulation time and then \
                    number of timesteps seperated by a space")

parser.add_argument("-bt", "--boundary_temp", type=float, default=1800.00,
	                help="Determines the temperature boundary \
                         condition at the outside of the particle")

parser.add_argument("-gd", "--g_dot", type=float, default=1.1E10,
                    help="Determines the generation in the fuel")

parser.add_argument("-tg", "--transient_gen", nargs='+', type=float,
                    default=[1.1E10, 1200], required=False,
	                help="Runs transient model. Enter simulation time and then \
                          number of timesteps seperated by a space")

args = parser.parse_args()

layers_per_node = args.layers_per_node

# Generate nested dictionary containing the materials, their radii,
# and their position in the particle

material_info = {}
material_info[args.fuel] = {'Radius': args.fuel_radius, 'Position': 0}

for i in range(len(args.clad)):
    material_info[args.clad[i]] = {'Radius': args.clad_radii[i],
                                   'Position': i+1}


material_props = material_properties.material_property_library(material_info)


mesh = generate_mesh.generate_mesh(material_props, layers_per_node)

print(args.transient)

boundary_condition = boundary_conditions.boundary_conditions(
                                       args.clad_radii[-1], args.boundary_temp)

# Run steady state model

if len(args.transient) == 0:
    A = build_matrix_A.build_matrix_A(material_props, mesh)
    b = build_matrix_b.build_matrix_b(boundary_condition[1],
                                      mesh, material_props, args.g_dot)

    temperature_array = matrix_solver.solve_matrix(A, b)

#    print(temperature_array)

    steady_state_plot.temperature_plot(temperature_array, mesh)

elif len(args.transient) == 2:
    time = generate_timesteps.generate_timesteps(args.transient[0],
                                                 args.transient[1])
    g_dot_list = [args.g_dot, args.transient_gen[0]]
    temp_boundary_list = [args.boundary_temp, args.transient_gen[1]]
    temperature_array = transient_model.transient_model(time, material_info,
                                                        mesh, g_dot_list,
                                                        temp_boundary_list)
    transient_plot.transient_plot(temperature_array, mesh)

