import tensorflow as tf

def real_valued_fast_fourier_transform(tensor):
    return tf.signal.rfft(tensor)
