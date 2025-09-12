import tensorflow as tf

# Example function to apply to each element
def transform_fn(x):
    return x * 2  # Example transformation: multiply by 2

# Create a sample tensor
input_tensor = tf.constant([[1, 2, 3], [4, 5, 6]])

# Unstack the tensor along axis 0
unstacked_tensors = tf.unstack(input_tensor, axis=0)

# Apply the transformation function to each unstacked tensor
transformed_tensors = [transform_fn(tensor) for tensor in unstacked_tensors]

# Stack back the transformed tensors along axis 0
output_tensor = tf.stack(transformed_tensors)

print(output_tensor)
