import tensorflow as tf

# Create a 1-D complex tensor
input = tf.complex([1 + 2j, 3 - 1j], [-2 - 1j, 4 + 3j])

# Compute the inverse real-valued fast Fourier transform
output = tf.raw_ops.IRFFT(input)

# Print the output tensor
print(output)
