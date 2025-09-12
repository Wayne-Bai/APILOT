import tensorflow as tf

# Define the function to apply to each element
def fn(x):
    return tf.square(x)

# Create a tensor
tensor = tf.constant([1.0, 2.0, 3.0, 4.0, 5.0])

# Unstack the tensor on axis 0
unstacked_tensor = tf.unstack(tensor, axis=0)

# Apply the function to each element
transformed_elements = tf.map_fn(fn, unstacked_tensor)

# Stack the transformed elements back into a tensor
transformed_tensor = tf.stack(transformed_elements)

# Print the original and transformed tensors
print("Original tensor:")
print(tensor)
print("\nTransformed tensor:")
print(transformed_tensor)
