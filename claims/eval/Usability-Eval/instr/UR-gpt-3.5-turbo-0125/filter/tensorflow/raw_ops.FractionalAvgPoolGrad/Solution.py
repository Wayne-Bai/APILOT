
import tensorflow as tf

def fractional_avg_pool_grad(input_size, pooled_gradients, rowpooling_sequence, colpooling_sequence, rowpooling_ratios, colpooling_ratios, overlapping, deterministic, name=None):
    return tf.raw_ops.FractionalAvgPoolGrad(input_size=input_size, pooled_gradients=pooled_gradients, rowpooling_sequence=rowpooling_sequence, colpooling_sequence=colpooling_sequence, rowpooling_ratios=rowpooling_ratios, colpooling_ratios=colpooling_ratios, overlapping=overlapping, deterministic=deterministic, name=name)
