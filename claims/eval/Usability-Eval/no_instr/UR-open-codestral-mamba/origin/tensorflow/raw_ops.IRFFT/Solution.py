import tensorflow as tf

def inverse_fft(input_tensor):
    return tf.signal.inverse_fft(input_tensor)

# Example usage
input_tensor = tf.constant([1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0], dtype=tf.complex64)
output_tensor = inverse_fft(input_tensor)
print(output_tensor)
