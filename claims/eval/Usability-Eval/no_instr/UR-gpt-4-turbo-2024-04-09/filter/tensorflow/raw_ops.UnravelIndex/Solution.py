import tensorflow as tf

def convert_flat_indices_to_coordinates(indices, shape):
    return tf.unstack(tf.transpose(tf.stack(tf.unravel_index(indices, shape))), axis=1)

# Example usage
shape = [10, 10]  # Shape of the tensor
flat_indices = [22, 45, 99]
coordinates = convert_flat_indices_to_coordinates(flat_indices, shape)
print(coordinates)
