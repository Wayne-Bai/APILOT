
import tensorflow as tf

@tf.function
def fractional_max_pool_grad(orig_input, orig_output, orig_grad, row_pooling_sequence, col_pooling_sequence, row_pooling_ratio, col_pooling_ratio):
    grad = tf.raw_ops.FractionalMaxPoolGrad(orig_input=orig_input, orig_output=orig_output, orig_grad=orig_grad, row_pooling_sequence=row_pooling_sequence, col_pooling_sequence=col_pooling_sequence, row_pooling_ratio=row_pooling_ratio, col_pooling_ratio=col_pooling_ratio)
    return grad
