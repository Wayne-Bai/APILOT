import tensorflow as tf

# Define a function to apply to each element
def apply_fn(element):
    return element * 2  # Example transform (multiplying each element by 2)

# Create a tensor
tensor = tf.constant([1.0, 2.0, 3.0, 4.0])

# Apply the function to each element
transformed_tensor = tf.map_fn(lambda x: tf.py_function(apply_fn, [x], tf.float32), tensor)

print(transformed_tensor)
