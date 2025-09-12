import tensorflow as tf

# Create a real-valued input signal
real_input = tf.constant([0.0, 1.0, 0.0, 0.0], dtype=tf.float32)

# Compute the RFFT
rfft_output = tf.signal.rfft(real_input)

# Print the result
print(rfft_output)
