import tensorflow as tf

# Example input raw bytes tensor
input_tensor = tf.constant([104, 101, 108, 108, 111, 32, 116, 104, 108, 109], dtype=tf.uint8)

# Decode raw bytes to string
decoded_string = tf.strings.unicode_decode(input_tensor, 'UTF-8')

# Convert decoded string tensor to a tensor of bytes
decoded_bytes = tf.strings.unicode_encode(decoded_string, 'UTF-8')

# Convert bytes tensor back to numpy array (if needed)
decoded_bytes_np = decoded_bytes.numpy()

print('Input Raw Bytes:', input_tensor.numpy())
print('Decoded Bytes:', decoded_bytes_numpy())
