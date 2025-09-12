import tensorflow as tf
import numpy as np

# For illustration purposes, let's create a 64-point random signal.
signal = tf.random.normal(shape=[64])

# Define dimension of our FFT analysis
N = 64

# We then need to pad the signal to a length that is a power of 2,
# which this function does for us.
num_fft = 1 << (int(np.ceil(np.log2(N))) + 1)
padded_signal = tf.signal.frame(signal, frame_length=num_fft, frame_step=num_fft)

# Now we perform the FFT.
ffts = tf.signal.fft(padded_signal)

# The FFT run across the last axis of the signal.
# So we need to specify the inverse FFT axis as -1 in the ifft function.
# We also need to resize the transformed signal to the original shape.
inverse_ffts = tf.signal.inverse_fft(ffts)
inverse_fft = inverse_ffts[..., -signal.shape[-1]:]
