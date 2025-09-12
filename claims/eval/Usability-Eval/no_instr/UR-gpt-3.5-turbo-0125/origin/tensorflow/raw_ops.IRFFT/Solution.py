
import tensorflow as tf

def inverse_real_valued_fft(input, fft_length):
    input = tf.cast(input, tf.complex64)
    input = tf.signal.ifft2d(input)
    return tf.cast(input, tf.float32)

# Example usage
input_data = tf.constant([[1.0, 2.0],
                          [3.0, 4.0]], dtype=tf.float32)
fft_length = input_data.shape[0] * input_data.shape[1]
output = inverse_real_valued_fft(input_data, fft_length)
print(output)
