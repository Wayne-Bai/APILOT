import tensorflow as tf

def create_dense_tensor(ragged_tensor):
    # Use tf.ragged.map_flat_values to extract the values of the ragged tensor
    flat_values = tf.ragged.map_flat_values(ragged_tensor)
    # Use tf.reshape to reshape the flattened values into a dense tensor with the desired shape
    dense_tensor = tf.reshape(flat_values, (-1, 1))
    return dense_tensor