import tensorflow as tf

# Define a simple function to transform each element
def transform_fn(element):
    # Example transformation: multiply each element by 2
    return element * 2

# Create a sample tensor
elems = tf.constant([[1, 2, 3], [4, 5, 6], [7, 8, 9]], dtype=tf.int32)

# Unstack elems on axis 0
unstacked_elems = tf.unstack(elems, axis=0)

# Apply the transformation function to each element
transformed_elems = [transform_fn(elem) for elem in unstacked_elems]

# Stack them back into a single tensor if needed
result = tf.stack(transformed_elems, axis=0)

# Print the result
print(result)
