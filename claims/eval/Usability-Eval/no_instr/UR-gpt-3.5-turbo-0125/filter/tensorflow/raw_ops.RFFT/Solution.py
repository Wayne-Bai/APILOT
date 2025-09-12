
import tensorflow as tf

def fft_real(input_tensor):
    fft_result = tf.signal.rfft(input_tensor)
    return fft_result

# Example usage
input_tensor = tf.constant([1.0, 2.0, 3.0, 4.0])
result = fft_real(input_tensor)
print(result)
