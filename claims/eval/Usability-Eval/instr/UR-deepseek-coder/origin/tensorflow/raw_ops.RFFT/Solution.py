import tensorflow as tf

def real_valued_fft(input_tensor):
    # Compute the FFT of the input tensor
    fft_result = tf.signal.fft(tf.cast(input_tensor, tf.complex64))
    
    # Extract the real part of the FFT result
    real_part = tf.math.real(fft_result)
    
    return real_part

# Example usage:
input_data = tf.constant([1.0, 2.0, 3.0, 4.0])
output = real_valued_fft(input_data)
print(output.numpy())
