import tensorflow as tf

# Define the transformation function
def transform_fn(x):
    # Example transformation: multiply each element by 2
    return x * 2

# Sample tensor
elems = tf.constant([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Apply the function to each element unstacked on axis 0
unstacked_elems = tf.unstack(elems, axis=0)
transformed_elems = [transform_fn(e) for e in unstacked_elems]

# Convert the list back to a tensor
result = tf.stack(transformed_elems, axis=0)

# Run a session to evaluate the tensor if in TensorFlow 1.x
# result = tf.compat.v1.Session().run(result)

print(result)
