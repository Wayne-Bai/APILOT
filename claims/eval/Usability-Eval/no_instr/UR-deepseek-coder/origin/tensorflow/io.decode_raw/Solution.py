import tensorflow as tf

def convert_bytes_to_numeric_tensor(input_tensor):
    # Convert the raw bytes tensor to a string tensor
    string_tensor = tf.io.decode_raw(input_tensor, tf.uint8)
    
    # Convert the string tensor to a numeric tensor (e.g., float32)
    numeric_tensor = tf.cast(string_tensor, tf.float32)
    
    return numeric_tensor

# Example usage:
# input_tensor = tf.constant(b'\x00\x01\x02\x03')  # Example raw bytes
# numeric_tensor = convert_bytes_to_numeric_tensor(input_tensor)
# print(numeric_tensor)
