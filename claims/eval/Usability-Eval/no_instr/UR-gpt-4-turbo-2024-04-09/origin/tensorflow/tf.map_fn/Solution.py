import tensorflow as tf

def apply_fn_to_elements(elems, fn):
    return tf.map_fn(fn, elems, dtype=tf.float32)  # Specify the appropriate dtype based on your function's requirements

# Example tensor and function
elems = tf.constant([[1.0, 2.0], [3.0, 4.0]])
fn = lambda x: x * 2

# Applying the function to each element
result = apply_fn_to_elements(elems, fn)
print(result)
