import tensorflow as tf

def inverse_fft(input_tensor):
    """
    Perform an inverse real-valued fast Fourier transform (IRFFT) on the input tensor.

    Parameters:
    input_tensor (tf.Tensor): Input tensor of real values.

    Returns:
    tf.Tensor: Output tensor containing the inverse FFT.
    """
    complex_tensor = tf.concatenate([input_tensor[:, None], tf.zeros_like(input_tensor[:, None])], axis=1)  # converting to complex
    complex_output = tf.signal.fft(complex_tensor)
    real_output = tf.real(complex_output)
    return real_output

# Example usage:
input_data = tf.constant([1.0, 2.0, 3.0, 4.0], dtype=tf.float32)
result = inverse_fft(input_data)
print(result.numpy())
