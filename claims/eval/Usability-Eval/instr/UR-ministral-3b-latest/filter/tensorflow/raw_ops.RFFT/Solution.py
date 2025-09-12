import tensorflow as tf

# Function to perform real-valued FFT
def real_fft(x):
    y = tf.signal.fft(x)
    return y

# Example usage
data = tf.constant([1.0, 2.0, 3.0, 4.0])
fft_data = real_fft(data)
print("Original data:", data.numpy())
print("FFT data:", fft_data.numpy())
