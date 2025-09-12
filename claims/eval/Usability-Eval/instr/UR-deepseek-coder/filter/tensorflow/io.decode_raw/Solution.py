import tensorflow as tf

def convert_raw_bytes_to_numeric_tensor(input_tensor):
    # Assuming the input tensor contains raw bytes
    # Convert the raw bytes to a numeric tensor
    numeric_tensor = tf.io.decode_raw(input_tensor, tf.float32)
    
    return numeric_tensor

# Example usage:
# input_tensor = tf.constant(b'\x00\x00\x80?\x00\x00\x00@\x00\x00@@')  # Example raw bytes
# numeric_tensor = convert_raw_bytes_to_numeric_tensor(input_tensor)
# print(numeric_tensor)
