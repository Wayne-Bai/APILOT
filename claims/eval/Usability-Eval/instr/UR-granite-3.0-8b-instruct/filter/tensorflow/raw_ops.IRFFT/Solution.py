import tensorflow as tf

def inverse_real_valued_fft(input_tensor):
    return tf.raw_ops.InverseRealValuedFFT(input_tensor)
