
import tensorflow as tf

def real_valued_fft(input_tensor):
    fft_result = tf.signal.rfft(input_tensor)
    return fft_result

# Example usage:
input_data = tf.constant([1.0, 2.0, 3.0, 4.0, 5.0])
result = real_valued_fft(input_data)
print(result)
