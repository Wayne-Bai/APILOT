
import tensorflow as tf

# Define the input tensor
input_tensor = tf.constant([1.0, 2.0, 3.0, 4.0])

# Apply Real-valued fast Fourier transform using tf.signal.rfft
fft_output = tf.signal.rfft(input_tensor)

# Print the output
print(fft_output)
