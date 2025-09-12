import tensorflow as tf

# Create a complex-valued input tensor
input = tf.complex(real=tf.random.normal([100]), imag=tf.random.normal([100]))

# Compute the inverse real-valued fast Fourier transform
fft_op = tf.raw_ops.FFT(input=input, fft_length=[100])

# Convert the output from complex to real-valued
output = tf.math.real(fft_op)

# Print the output tensor
print(output)
