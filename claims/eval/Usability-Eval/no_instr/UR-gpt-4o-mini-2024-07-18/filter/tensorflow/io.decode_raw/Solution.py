import tensorflow as tf

def convert_raw_bytes_to_numeric_tensor(raw_bytes_tensor):
    # Decode the raw bytes input tensor to string, then convert them to a numeric tensor
    # Assuming the raw bytes should be converted to integers. Adjust the data type if necessary.
    string_tensor = tf.strings.to_number(tf.strings.decode_raw(raw_bytes_tensor, tf.uint8), tf.int32)
    
    return string_tensor

# Example usage
raw_bytes = tf.constant(b'\x00\x01\x02\x03', dtype=tf.string)
numeric_tensor = convert_raw_bytes_to_numeric_tensor(raw_bytes)
print(numeric_tensor)
