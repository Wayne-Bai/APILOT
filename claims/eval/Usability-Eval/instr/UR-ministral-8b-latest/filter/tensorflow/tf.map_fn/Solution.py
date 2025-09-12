import tensorflow as tf

# Define the transformation function
def example_transform_function(element):
    return element * 2

# Create example tensor
tensor = tf.constant([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Apply transformation function to each element unstacked on axis 0
transformed_tensor = tf.map_fn(example_transform_function, tensor, fn_in_axis=None)

# Print the transformed tensor
print(transformed_tensor)
