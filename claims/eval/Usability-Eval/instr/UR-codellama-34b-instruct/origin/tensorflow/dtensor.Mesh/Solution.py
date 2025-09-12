
import tensorflow as tf

# Define the list of mesh dimensions
dimensions = [3, 4, 5]

# Create a mesh grid for each dimension
mesh_grids = []
for dim in range(len(dimensions)):
    mesh_grids.append(tf.meshgrid(range(dimensions[dim]), indexing='ij'))

# Concatenate the mesh grids along the last axis
mesh = tf.concat([mesh_grid for mesh_grid in mesh_grids], axis=-1)
