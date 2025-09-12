import tensorflow as tf

def bytes_to_numeric_tensor(input_tensor):
    # Decode the bytes in the input tensor
    decoded_tensor = tf.io.decode_raw(input_tensor, tf.uint8)

    # Convert the decimal values in the tensor to floating point numbers
    numeric_tensor = tf.cast(decoded_tensor, tf.float32)

    return numeric_tensor
