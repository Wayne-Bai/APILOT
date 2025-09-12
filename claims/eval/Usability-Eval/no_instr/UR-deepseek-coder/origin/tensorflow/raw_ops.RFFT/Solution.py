import tensorflow as tf

def real_valued_fft(input_tensor):
    # Compute the FFT of the input tensor
    fft_result = tf.signal.rfft(input_tensor)
    
    # Extract the real and imaginary parts
    real_part = tf.math.real(fft_result)
    imaginary_part = tf.math.imag(fft_result)
    
    # Combine real and imaginary parts into a complex tensor
    complex_result = tf.complex(real_part, imaginary_part)
    
    return complex_result

# Example usage:
input_data = tf.constant([1.0, 2.0, 3.0, 4.0], dtype=tf.float32)
fft_output = real_valued_fft(input_data)
print(fft_output)
