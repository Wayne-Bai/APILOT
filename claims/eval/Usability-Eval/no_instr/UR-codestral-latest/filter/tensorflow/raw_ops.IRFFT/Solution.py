import tensorflow as tf

# Assume you have a complex tensor `fft_tensor` generated using `tf.signal.fft`
fft_tensor = ...

# Here's how you can use the irfft function
original_tensor = tf.signal.irfft(fft_tensor)
