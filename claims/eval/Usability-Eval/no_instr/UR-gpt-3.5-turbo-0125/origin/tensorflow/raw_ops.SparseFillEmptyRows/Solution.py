
import tensorflow as tf

def fill_empty_rows(input_indices, default_value):
    filled_sparse_tensor = tf.sparse.fill_empty_rows(input_indices, default_value)
    return filled_sparse_tensor

# Example usage
input_indices = tf.constant([[0, 0], [1, 2], [2, 1]])
default_value = tf.constant(0)
filled_tensor = fill_empty_rows(input_indices, default_value)
print(filled_tensor)
