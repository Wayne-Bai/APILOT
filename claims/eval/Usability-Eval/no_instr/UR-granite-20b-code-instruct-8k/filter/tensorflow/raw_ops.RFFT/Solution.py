import tensorflow as tf

# Define the input tensor
input_tensor = tf.constant([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])

# Perform the Real-valued fast Fourier transform
fft_output = tf.signal.fft(input_tensor)

# Print the output of the FFT
print(fft_output.numpy())
