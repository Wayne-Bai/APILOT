import tensorflow as tf
def dequantize(input, min_range, max_range, mode="MIN_FIRST", dtype=tf.float32):
    return tf.raw_ops.Dequantize(input=input, min_range=min_range, max_range=max_range, mode=mode, T=dtype)
