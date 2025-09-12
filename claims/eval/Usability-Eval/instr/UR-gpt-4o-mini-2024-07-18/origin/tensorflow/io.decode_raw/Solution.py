import tensorflow as tf

# Function to convert raw bytes from an input tensor to numeric tensors
def convert_raw_bytes_to_numeric(input_tensor):
    # Assuming input_tensor is of type tf.Tensor and contains raw byte strings
    # Decode the raw bytes and convert to a numeric tensor
    numeric_tensor = tf.io.decode_raw(input_tensor, tf.float32)  # Change tf.float32 to desired numeric type if necessary
    return numeric_tensor

# Example usage
raw_bytes_tensor = tf.constant([b'\x00\x00\x80?', b'\x00\x00\xa0@'])  # Raw bytes example
numeric_tensor = convert_raw_bytes_to_numeric(raw_bytes_tensor)
print(numeric_tensor)
