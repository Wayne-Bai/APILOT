import tensorflow as tf

def fractional_avg_pool_gradient(input, output, row_pooling_ratio, col_pooling_ratio, seed=None):
    return tf.raw_ops.FractionalAvgPoolGrad(
        orig_input=input,
        orig_output=output,
        row_pooling_ratio=row_pooling_ratio,
        col_pooling_ratio=col_pooling_ratio,
        seed=seed
    )
