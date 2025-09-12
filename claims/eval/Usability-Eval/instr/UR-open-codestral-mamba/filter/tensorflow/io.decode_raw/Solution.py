import tensorflow as tf

# Prepare the input tensor with some sample b'\x01\x02\x03\x04' values
data = tf.constant([b'\x01\x02\x03\x04', b'\x05\x06\x07\x08', b'\x09\x0a\x0b\x0c'])

# Convert raw bytes to int32 tensor using tf.decode_raw
input_tensor = tf.io.decode_raw(data, tf.int32)

# Print the input and output tensors
print("Original input:", data)
print("Numeric tensor:", input_tensor)

# Run the session to evaluate the tensors
with tf.Session() as sess:
    input_data, output_data = sess.run([data, input_tensor])
    print("Original input evaluation:", input_data.eval())
    print("Numeric tensor evaluation:", output_data.eval())
