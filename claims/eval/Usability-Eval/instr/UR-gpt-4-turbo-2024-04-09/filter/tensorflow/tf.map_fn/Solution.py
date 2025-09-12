import tensorflow as tf

def apply_fn_to_elements(elems, fn):
    return tf.map_fn(fn, elems)

# Example usage
elems = tf.constant([[1, 2], [3, 4], [5, 6]])
result = apply_fn_to_elements(elems, lambda x: x * 2)
print(result)
