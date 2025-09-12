import tensorflow as tf

# Define the function to apply to each element
def fn(element):
    # For demonstration, assume fn just multiplies each element by 2
    return element * 2

# Define a sample tensor
elems = tf.constant([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Use tf.map_fn to apply the function along the specified axis
result = tf.map_fn(fn, elems, fn_output_signature=tf.TensorSpec(shape=(3,), dtype=tf.int32))

print(result)
