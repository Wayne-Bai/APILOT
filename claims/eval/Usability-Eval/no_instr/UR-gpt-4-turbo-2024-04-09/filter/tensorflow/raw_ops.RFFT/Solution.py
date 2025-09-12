import tensorflow as tf

# Sample data: a 1D array of real numbers
data = [0.0, 1.0, -1.0, 0.0]

# Convert the data to a TensorFlow tensor
tensor = tf.constant(data, dtype=tf.float32)

# Compute the Real-valued fast Fourier Transform
fft_result = tf.signal.rfft(tensor)

print("FFT Result:", fft_result.numpy())
