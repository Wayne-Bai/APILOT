
import tensorflow as tf

def fractional_avg_pool(input, pooling_ratio=[1.0, 2.0, 2.0, 1.0], pseudo_random=False, overlapping=False):
    return tf.raw_ops.FractionalAvgPool(input=input, pooling_ratio=pooling_ratio, pseudo_random=pseudo_random, overlapping=overlapping)

# Example usage
input_tensor = tf.constant(...)
output = fractional_avg_pool(input_tensor, pooling_ratio=[1.0, 2.0, 2.0, 1.0], pseudo_random=False, overlapping=False)
