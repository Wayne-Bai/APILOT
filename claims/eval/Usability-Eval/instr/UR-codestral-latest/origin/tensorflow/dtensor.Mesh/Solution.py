import tensorflow as tf
import numpy as np

def mesh_config(mesh_dims):
    # Create an empty list to hold the variables for each mesh dimension
    mesh_vars = []

    # Loop through each mesh dimension
    for i, dim in enumerate(mesh_dims):
        # Create a new variable for this dimension
        var = tf.Variable(np.random.randn(dim, dim), name=f"mesh_var_{i}")
        # Add the variable to our list
        mesh_vars.append(var)

    # Return the list of variables
    return mesh_vars

# Define our mesh dimensions
mesh_dims = [10, 20, 30]
# Create our mesh configuration
mesh_vars = mesh_config(mesh_dims)

# Print out the shape of each variable to verify they were created correctly
for i, var in enumerate(mesh_vars):
    print(f"Mesh variable {i} shape: {var.shape}")
