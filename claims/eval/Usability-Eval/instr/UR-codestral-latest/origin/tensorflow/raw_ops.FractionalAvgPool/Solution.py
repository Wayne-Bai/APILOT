import tensorflow as tf

def fractional_avg_pool(input_tensor, pooling_ratio):
    pool_size = [1, pooling_ratio, pooling_ratio, 1]
    strides = [1, pooling_ratio, pooling_ratio, 1]
    output_size = [tf.shape(input_tensor)[0], tf.math.ceil(tf.shape(input_tensor)[1] / pooling_ratio), tf.math.ceil(tf.shape(input_tensor)[2] / pooling_ratio), tf.shape(input_tensor)[3]]
    paddings = [[0, 0], [0, tf.maximum(output_size[1] * pooling_ratio - tf.shape(input_tensor)[1], 0)], [0, tf.maximum(output_size[2] * pooling_ratio - tf.shape(input_tensor)[2], 0)], [0, 0]]
    padded_tensor = tf.pad(input_tensor, paddings, "CONSTANT")
    avg_pooled = tf.nn.avg_pool(padded_tensor, ksize=pool_size, strides=strides, padding="VALID")
    return avg_pooled
