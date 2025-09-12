
import tensorflow as tf

def gather_ragged_slices(params, indices):
    return tf.gather(params, indices, axis=0)

# Example Usage
params = tf.constant([[1, 2], [3, 4], [5, 6]])
indices = tf.ragged.constant([[0], [2]])
result = gather_ragged_slices(params, indices)
print(result)
