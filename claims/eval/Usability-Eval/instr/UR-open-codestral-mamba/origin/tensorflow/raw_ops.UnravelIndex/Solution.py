import tensorflow as tf

# Define the input tensor
input_tensor = tf.constant([1, 5, 3])

# Get the meshgrid from the input tensor
x_coords, y_coords, z_coords = tf.raw_ops.Meshgrid(dim1=input_tensor, dim2=input_tensor, dim3=input_tensor)

# Print the coordinates
print(x_coords)
print(y_coords)
print(z_coords)
