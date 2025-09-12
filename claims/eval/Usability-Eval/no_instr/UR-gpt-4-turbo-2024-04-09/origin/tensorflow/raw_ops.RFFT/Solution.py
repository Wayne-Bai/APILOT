import tensorflow as tf

# Create a tensor to apply FFT
tensor = tf.constant([1.0, 2.0, 3.0, 4.0])

# Apply the real-valued fast Fourier transform
fft_result = tf.signal.rfft(tensor)

print("FFT Result:", fft_result.numpy())
