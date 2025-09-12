# Importing the necessary libraries
import tensorflow as tf

# Define the shape of the input data
batch_shape = [2]
signal_shape = [128]

# Create a tensor with random values
signal = tf.random.uniform(signal_shape)

# Use tf.signal.fft to calculate the FFT
fft_result = tf.signal.fft(tf.signal.rfft(signal))

# Invert the FFT
inverse_fft_result = tf.signal.irfft(fft_result, signal_shape)

print(inverse_fft_result)
