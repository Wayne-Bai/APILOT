import tensorflow as tf

def convert_raw_to_numeric(raw_tensor):
    """Convert raw bytes from input tensor into numeric tensor."""
    # Use tf.io.decode_raw to convert raw bytes to a Tensor
    numeric_tensor = tf.io.decode_raw(raw_tensor, tf.float32)
    return numeric_tensor

# Example usage:
# Create a raw tensor
raw_tensor = tf.constant([0, 1, 2, 3, 4], dtype=tf.uint8)

# Convert raw tensor to numeric tensor
numeric_tensor = convert_raw_to_numeric(raw_tensor)

# Print the converted tensor
print(numeric_tensor)
