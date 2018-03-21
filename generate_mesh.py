

def generate_mesh(layer_outer_radii,nodes_per_layer):
   """ This function generates an array of grid points in the radial direction, or mesh. Grid points are spaced evenly between the previous outer radii (zero for the first layer) and the specified outer radii. generate_mesh returns a single array of r values

   inputs
   ------
   - layer_outer_radii : list of radii for each layer of the fuel particle. The first layer is assumed to start at r=0
   - nodes_per_layer : list with the number of grid points corresponding to each layer

   outputs
   -------
   - mesh : a list of grid points
   """
   
   import numpy as np
   mesh=np.zeros(sum(nodes_per_layer))
   nodes_sum=0
   for i in range(1, len(layer_outer_radii)):
      nodes_sum_new=nodes_sum+nodes_per_layer[i-1]
      single_material_nodes=np.linspace(layer_outer_radii[i-1],layer_outer_radii[i],nodes_per_layer[i-1])
      mesh[nodes_sum:nodes_sum_new]=single_material_nodes
      nodes_sum=nodes_sum_new