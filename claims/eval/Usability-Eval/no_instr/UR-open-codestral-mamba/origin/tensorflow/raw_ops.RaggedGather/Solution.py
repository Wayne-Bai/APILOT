import tensorflow as tf

def gather_ragged_slices(params, indices):
    # Convert indices to int32 for TensorFlow 2.x
    indices = tf.cast(indices, tf.int32)

    # Get the range for each index
    range_tensor = tf.expand_dims(tf.range(tf.shape(indices)[0]), 1)

    # Create indices for the gather operation
    full_indices = tf.concat([range_tensor, indices], 1)

    # Perform the gather operation on the params axis
    result = tf.gather_nd(params, full_indices)

    # "Padding" the result because TensorFlow 2.x doesn't have default padding value
    # Here we use 0 as padding value. You may wish to change this based on your application
    padding = tf.zeros_like(indices)
    result = tf.where(indices >= tf.shape(params)[0], padding, result)

    return result
