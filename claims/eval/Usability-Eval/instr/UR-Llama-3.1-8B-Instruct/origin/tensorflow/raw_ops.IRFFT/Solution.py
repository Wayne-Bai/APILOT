# Import the required library
import tensorflow as tf
from tensorflow.python.ops import dnn_ops
from tensorflow.python.framework import dtypes

def inverse_real_valued_fast_fourier_transform(input_tensor, signal_ndims, fft_length, name=None):
    """
    Computes the inverse real-valued fast Fourier transform.

    Args:
        input_tensor: A tensor.
        signal_ndims: An integer.
        fft_length: An integer.
        name: A string.

    Returns:
        A complex tensor.
    """
    return tf.raw_ops.InverseFFT(input=input_tensor,
                                 fft_length=fft_length,
                                 name=name)

# Create a sample input tensor
input_tensor = tf.random.uniform([16, 8])

# Compute the inverse real-valued fast Fourier transform
output = inverse_real_valued_fast_fourier_transform(input_tensor,
                                                    signal_ndims=1,
                                                    fft_length=8,
                                                    name='my_inverse_fft')
