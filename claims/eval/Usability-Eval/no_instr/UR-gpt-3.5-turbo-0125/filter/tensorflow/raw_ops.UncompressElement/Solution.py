
import tensorflow as tf

@tf.function
def uncompress_data(compressed_data):
    uncompressed_data = tf.raw_ops.DecodeRaw(input_bytes=compressed_data, out_type=tf.string)
    return uncompressed_data
