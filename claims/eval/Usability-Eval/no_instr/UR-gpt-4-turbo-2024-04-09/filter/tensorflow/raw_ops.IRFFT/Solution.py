import tensorflow as tf

# Create an example tensor, here using a complex number tensor as an input
data = tf.constant([complex(1, 2), complex(3, 4), complex(5, 6), complex(7, 8)], dtype=tf.complex64)

# Compute the real-valued inverse FFT
inverse_fft = tf.signal.irfft(data)

print("Inverse Real FFT:", inverse_fft.numpy())
