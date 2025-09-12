import tensorflow as tf

# Define a function to apply to each element
def apply_function(elem):
    return elem * 2  # Example: doubling each element

# Create a tensor to demonstrate the transformation
tensor = tf.constant([[1, 2, 3], [4, 5, 6]], dtype=tf.float32)

# Use tf.map_fn along with unstacking to apply the function to each element along axis 0
unstacked = tf.unstack(tensor, axis=0)
mapped = tf.map_fn(lambda x: apply_function(x), unstacked, dtype=tf.int32)
result = tf.stack(mapped)

print(result.numpy())
