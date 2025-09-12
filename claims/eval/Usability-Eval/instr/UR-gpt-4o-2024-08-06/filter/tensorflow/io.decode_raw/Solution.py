import tensorflow as tf

# Example raw byte input tensor
raw_byte_tensor = tf.constant([b'1', b'2', b'3', b'4', b'5'])

# Define a function to convert raw bytes to numeric tensors
def bytes_to_numeric(byte_tensor):
    # Convert byte tensor to string tensor
    string_tensor = tf.strings.bytes_split(byte_tensor)
    
    # Convert string tensor to numeric tensor
    numeric_tensor = tf.strings.to_number(string_tensor, out_type=tf.int32)
    
    return numeric_tensor

# Apply the conversion function to the raw byte tensor
numeric_tensor = bytes_to_numeric(raw_byte_tensor)

# Print the resulting numeric tensor
print(numeric_tensor.numpy())
