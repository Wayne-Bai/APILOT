
import tensorflow as tf

def unravel_indices(indices, shape):
    unraveled_coords = tf.unravel_index(indices, shape)
    return unraveled_coords

# Example usage
indices = tf.constant([5, 13, 29])
shape = (6, 6)
unraveled_coords = unravel_indices(indices, shape)
print(unraveled_coords)
