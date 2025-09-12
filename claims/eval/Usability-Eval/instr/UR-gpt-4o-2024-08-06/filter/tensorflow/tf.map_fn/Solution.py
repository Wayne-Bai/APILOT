import tensorflow as tf

# Define a function to be applied to each element
def transform_fn(x):
    return x * 2  # Example transformation: multiplying each element by 2

# Create a TensorFlow tensor with some sample data
elems = tf.constant([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Unstack the tensor along axis 0
unstacked_elems = tf.unstack(elems, axis=0)

# Apply the transform function to each element
transformed_elems = [transform_fn(elem) for elem in unstacked_elems]

# Optional: Stack the transformed elements back
result = tf.stack(transformed_elems, axis=0)

# Print the result
print(result.numpy())
