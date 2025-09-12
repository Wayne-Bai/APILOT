
import tensorflow as tf

@tf.function
def convert_flat_indices_to_coords(flat_indices, shape):
    dims = tf.shape(shape)[0]
    coords = tf.raw_ops.FlatToCoord(
        indices=flat_indices,
        output_shape=shape,
        end_index=dims
    )
    return coords

# Example usage
flat_indices = tf.constant([0, 1, 2, 3, 4, 5])
shape = tf.constant([2, 3])
coords = convert_flat_indices_to_coords(flat_indices, shape)
print(coords)
