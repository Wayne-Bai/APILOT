import tensorflow as tf
import numpy as np

# Create a signal of 256 points
signal = np.sin(np.arange(256) * 0.1)

# Convert the signal to a tensor
signal_tensor = tf.convert_to_tensor(signal, dtype=tf.float32)

# Compute the 1-dimensional Fourier transform
fft = tf.signal.fft(signal_tensor)

# Apply an inverse Fourier transform
signal_inverse = tf.signal.ifft(fft)

# Convert the signal back to numpy array
signal_inverse_np = signal_inverse.numpy()
