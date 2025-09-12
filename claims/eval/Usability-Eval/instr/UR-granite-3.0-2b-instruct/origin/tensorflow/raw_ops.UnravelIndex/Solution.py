import tensorflow as tf

def flat_to_coords(flat_indices):
    # Create a tensor of shape (batch_size, num_features) with the given flat indices
    flat_indices_tensor = tf.reshape(flat_indices, [-1, tf.shape(flat_indices)[-1]])

    # Calculate the coordinates using the reshape operation
    coords = tf.stack([tf.range(tf.shape(flat_indices_tensor)[0]), flat_indices_tensor], axis=-1)

    # Split the coordinates tensor into x and y coordinates
    x, y = tf.unstack(coords, axis=-1)

    return x, y

# Example usage:
flat_indices = tf.constant([[0, 1, 2], [3, 4, 5]], dtype=tf.int32)
x, y = flat_to_coords(flat_indices)

print("X coordinates:", x.numpy())
print("Y coordinates:", y.numpy())
