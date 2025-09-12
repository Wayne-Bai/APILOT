import tensorflow as tf

# Create a tensor with real values
real_values = tf.random.normal([128, 128])

# Perform the fast Fourier transform
fft = tf.signal.fft(real_values)

# Print the result
print(fft)
