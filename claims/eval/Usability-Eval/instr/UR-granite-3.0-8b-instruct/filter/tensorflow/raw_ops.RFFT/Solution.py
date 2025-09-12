import tensorflow as tf

# Assuming 'signal' is your input signal
signal = tf.constant([1.0, 2.0, 3.0, 4.0], dtype=tf.float32)

# Compute the real-valued fast Fourier transform
fft = tf.raw_ops.FFT(input=signal)

# To get the complex-valued result, you can use tf.abs(fft)
# If you want the real-valued result, you can use tf.real(fft)
