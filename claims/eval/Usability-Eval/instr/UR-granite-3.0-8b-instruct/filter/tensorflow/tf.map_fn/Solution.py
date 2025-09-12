import tensorflow as tf

def transform_elements(elements, fn):
    return tf.map_fn(fn, elements, parallel_iterations=10)

# Example usage:
# elements = tf.constant([[1, 2, 3], [4, 5, 6]])
# fn = lambda x: x * 2
# transformed_elements = transform_elements(elements, fn)
