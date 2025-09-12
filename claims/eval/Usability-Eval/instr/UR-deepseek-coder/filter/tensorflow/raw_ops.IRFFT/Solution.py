import tensorflow as tf

def inverse_real_fft(input_tensor):
    # Compute the inverse real-valued fast Fourier transform
    inverse_fft = tf.signal.irfft(input_tensor)
    return inverse_fft

# Example usage:
# input_tensor = tf.complex(tf.random.normal([4, 4]), tf.random.normal([4, 4]))
# result = inverse_real_fft(input_tensor)
# print(result)
