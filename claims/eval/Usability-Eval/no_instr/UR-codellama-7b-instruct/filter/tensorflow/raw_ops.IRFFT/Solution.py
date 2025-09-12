
import tensorflow as tf
from tensorflow import raw_ops

# Define the FFT op
fft = raw_ops.FFT(input=tf.random.normal([8, 8]), fft_length=16)

# Define the IFFT op
ifft = raw_ops.IFFT(input=fft, fft_length=16)

# Print the output of the FFT and IFFT ops
print("FFT:", fft)
print("IFFT:", ifft)
