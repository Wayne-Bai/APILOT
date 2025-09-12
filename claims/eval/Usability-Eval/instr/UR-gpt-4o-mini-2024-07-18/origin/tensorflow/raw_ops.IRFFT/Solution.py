import tensorflow as tf

def inverse_fft(signal):
    # Perform the inverse fast Fourier transform
    return tf.signal.ifft(signal)

# Example usage
# Create a sample complex-valued tensor
signal = tf.constant([[0.0, 1.0], [1.0, 0.0]], dtype=tf.complex64)

# Compute the inverse FFT
inverse_transform = inverse_fft(signal)

# Print the result
print(inverse_transform)
