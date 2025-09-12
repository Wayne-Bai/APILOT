import tensorflow as tf

def convert_raw_bytes_to_numeric_tensors(raw_bytes):
    # Decode raw bytes to string tensor and then convert to numeric tensor
    decoded_string_tensor = tf.io.decode_raw(raw_bytes, tf.uint8)
    numeric_tensor = tf.cast(decoded_string_tensor, tf.float32)
    
    return numeric_tensor

# Example of usage:
# This is just a simple example, replace `raw_input_bytes` with actual raw bytes input tensor.
raw_input_bytes = tf.constant(b'\x01\x02\x03\x04', dtype=tf.string)
numeric_tensor = convert_raw_bytes_to_numeric_tensors(raw_input_bytes)
print(numeric_tensor)
