import tensorflow as tf

# Function to convert raw bytes input tensor into numeric tensors of a specific dtype
def convert_bytes_to_numeric(bytes_tensor, dtype=tf.float32):
    # Decode the raw bytes to a string
    string_tensor = tf.io.decode_raw(bytes_tensor, tf.uint8)
    
    # Convert the decoded string to the desired numeric data type
    numeric_tensor = tf.cast(string_tensor, dtype)
    
    return numeric_tensor

# Example usage
# Creating a raw bytes tensor using an image example
raw_bytes_tensor = tf.constant(b'\x00\x01\x02\x03\x04', dtype=tf.string)

# Convert the raw bytes tensor to a numeric tensor
numeric_tensor = convert_bytes_to_numeric(raw_bytes_tensor)

print(numeric_tensor)
