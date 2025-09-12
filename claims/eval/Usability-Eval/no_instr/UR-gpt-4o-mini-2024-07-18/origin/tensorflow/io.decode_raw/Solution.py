import tensorflow as tf

def convert_raw_bytes_to_numeric_tensor(raw_bytes_tensor):
    # Decode the raw bytes to string
    string_tensor = tf.io.decode_raw(raw_bytes_tensor, tf.float32)
    
    # Convert the string tensor to numeric tensor
    numeric_tensor = tf.strings.to_number(string_tensor, out_type=tf.float32)
    
    return numeric_tensor

# Example usage:
raw_bytes = tf.constant(b'\x00\x00\x80\x3f\x00\x00\xa0\x3f', dtype=tf.string)  # Example raw bytes
numeric_tensor = convert_raw_bytes_to_numeric_tensor(raw_bytes)
print(numeric_tensor)
