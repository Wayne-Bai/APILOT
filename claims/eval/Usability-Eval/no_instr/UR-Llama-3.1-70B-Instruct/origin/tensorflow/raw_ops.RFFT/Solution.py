import tensorflow as tf

def real_fft(x, fft_length):
    """
    Real-valued fast Fourier transform.

    Args:
        x (tf.Tensor): A real-valued tensor.
        fft_length (int): The length of the FFT.

    Returns:
        tf.Tensor: The FFT of the input tensor.
    """
    x = tf.reshape(x, (-1, fft_length))
    batch_shape = tf.shape(x)[:-1]
    new_x = tf.signal.rfft(x)
    return tf.reshape(new_x, (*batch_shape, -1))

# Example usage:
x = tf.random.normal((32, 256))  # Create a random tensor
fft_length = 256
fft_result = real_fft(x, fft_length)
print(fft_result.shape)
