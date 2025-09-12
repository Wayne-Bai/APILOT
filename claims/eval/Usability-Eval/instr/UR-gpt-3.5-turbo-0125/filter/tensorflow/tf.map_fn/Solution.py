
import tensorflow as tf

# Define a custom map function
def map_fn(fn, elems):
    return tf.map_fn(fn, elems, fn.dtype)

# Define the transformation function
def transform_fn(elem):
    return elem * 2

# Define the input tensor
input_tensor = tf.constant([[1, 2, 3], [4, 5, 6]])

# Apply the transformation using the custom map function
output_tensor = map_fn(transform_fn, input_tensor)

# Display the output
print(output_tensor)
