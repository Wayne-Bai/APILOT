
import tensorflow as tf

@tf.function(input_signature=[tf.TensorSpec([10, 2], dtype=tf.float32)])
def fractional_avg_pool(x):
    # Implement your own gradient computation using the TensorFlow backend
    return tf.raw_ops.FractionalAvgPool(input=x, pooling_ratio=0.5, padding="SAME", strides=None)
