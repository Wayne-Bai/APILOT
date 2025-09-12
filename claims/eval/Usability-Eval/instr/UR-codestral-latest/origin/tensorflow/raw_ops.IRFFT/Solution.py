import tensorflow as tf

# Assuming 'fft' is a complex tensor
fft = tf.complex(real, imag)  # replace 'real' and 'imag' with your actual data

# Compute the IRFFT of the 'fft' tensor
irfft = tf.signal.irfft(fft)
