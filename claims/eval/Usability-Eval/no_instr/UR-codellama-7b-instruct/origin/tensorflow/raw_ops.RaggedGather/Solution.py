
import tensorflow as tf

# Define a function to gather ragged slices from params according to indices
def gather_ragged(params, indices):
    # Use tf.gather_nd to gather the ragged slices from params
    gathered = tf.gather_nd(params, indices)
    return gathered

# Test the function with some example inputs
inputs = [tf.ragged.constant([[1, 2], [3]]),
          tf.ragged.constant([[4, 5], [6, 7]])]
indices = tf.ragged.constant([[0, 1], [1, 0]])
gathered = gather_ragged(inputs, indices)
print("Gathered:", gathered)
