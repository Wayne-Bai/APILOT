import tensorflow as tf

def inverse_fft(x, fft_length=None):
    # Ensure that the input tensor has a complex dtype
    if not tf.is_complex(x.dtype):
        raise ValueError("Input tensor must be of a complex dtype.")
        
    # Compute the inverse FFT
    if fft_length is not None:
        return tf.signal.fftshift(tf.signal.fft(tf.signal.ifftshift(x, axes=-1), fft_length=fft_length), axes=-1)
    else:
        return tf.signal.fftshift(tf.signal.fft(tf.signal.ifftshift(x, axes=-1)))

# Example usage
x_complex = tf.constant([[1.0 + 1.0j, 2.0 + 2.0j], [3.0 + 3.0j, 4.0 + 4.0j]])
inverse_result = inverse_fft(x_complex)

print(inverse_result)
