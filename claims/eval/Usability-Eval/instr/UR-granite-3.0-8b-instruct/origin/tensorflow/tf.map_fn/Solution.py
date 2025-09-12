import tensorflow as tf

# Assuming you have a tensor 'tensor' and a function 'fn'
# Apply fn to each element of tensor unstacked on axis 0
def apply_fn_to_each_element(tensor, fn):
    return tf.map_fn(fn, tensor, dtype=tf.float32)

# Example usage:
# tensor = tf.constant([1, 2, 3, 4, 5])
# fn = lambda x: x * 2
# result = apply_fn_to_each_element(tensor, fn)
# print(result)
