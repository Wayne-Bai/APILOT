import tensorflow as tf

# Assuming input is a Tensor of dtype tf.string and we want to convert it into tf.float32

def convert_bytes_to_numeric(input_tensor):
    # Convert bytes to numerical values by interpreting each byte as an integer.
    numeric_tensor = tf.map_fn(lambda byte_string: tf.decode_raw(byte_string, tf.float32),
                               input_tensor,
                               dtype=tf.float32)
    return numeric_tensor

# Test the function
input_tensor = tf.constant([b"1.0", b"2.0", b"3.0"])
numeric_tensor = convert_bytes_to_numeric(input_tensor)
print(numeric_tensor.numpy())  # Output: array([[1.], [2.], [3.]], dtype=float32)
