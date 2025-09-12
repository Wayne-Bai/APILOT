import tensorflow as tf

# Define a real-valued signal as a Tensor
real_signal = tf.constant([1.0, 2.0, 3.0, 4.0], dtype=tf.float32)

# Compute the fast Fourier transform (FFT) of the real-valued signal
fft_result = tf.signal.fft(tf.cast(real_signal, tf.complex64))

# Print the result
print("FFT of the real signal:", fft_result.numpy())
