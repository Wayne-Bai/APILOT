import tensorflow as tf

def inverse_real_valued_fast_fourier_transform(input_tensor):
    return tf.raw_ops.IFFT(input=input_tensor)
