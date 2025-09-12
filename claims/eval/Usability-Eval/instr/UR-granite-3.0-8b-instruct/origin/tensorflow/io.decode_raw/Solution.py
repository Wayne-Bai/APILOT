import tensorflow as tf

def convert_bytes_to_numeric(input_tensor):
    # Ensure the input tensor is of type bytes
    assert input_tensor.dtype == tf.string

    # Convert bytes to numeric tensors using tf.io.decode_raw
    numeric_tensor = tf.io.decode_raw(input_tensor, tf.float32)

    # Reshape the numeric tensor to the desired shape
    # For example, if the input tensor has shape (batch_size, seq_length)
    # and each byte represents a float32 value, the numeric tensor will have shape (batch_size, seq_length, 4)
    # We can reshape it to (batch_size, seq_length) by taking the mean of the last dimension
    numeric_tensor = tf.reduce_mean(numeric_tensor, axis=-1)

    return numeric_tensor
