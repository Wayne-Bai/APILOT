
import tensorflow as tf

def fft_real(input_tensor):
    fft_output = tf.signal.fft(tf.cast(input_tensor, tf.complex64))
    return tf.abs(fft_output)

# Example usage
input_tensor = tf.constant([1.0, 2.0, 3.0, 4.0], dtype=tf.float32)
result = fft_real(input_tensor)
print(result)
