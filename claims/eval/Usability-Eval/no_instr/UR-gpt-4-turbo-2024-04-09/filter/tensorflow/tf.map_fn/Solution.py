import tensorflow as tf

def transform_elements(elems, fn):
    return tf.map_fn(fn, elems, fn_output_signature=elems.dtype)

# Example usage
elems = tf.constant([1, 2, 3, 4, 5])
result = transform_elements(elems, lambda x: x * x)
print(result)
