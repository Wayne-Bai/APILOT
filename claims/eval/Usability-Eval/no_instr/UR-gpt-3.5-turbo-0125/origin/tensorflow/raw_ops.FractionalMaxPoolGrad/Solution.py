
import tensorflow as tf

@tf.function
def compute_fractional_max_pool_gradient(orig_input, orig_pool, orig_output, grad, row_pooling_sequence, col_pooling_sequence, row_pooling_ratios, col_pooling_ratios):
    return tf.raw_ops.FractionalMaxPoolGrad(orig_input=orig_input, orig_pool=orig_pool, orig_output=orig_output, grad=grad, row_pooling_sequence=row_pooling_sequence, col_pooling_sequence=col_pooling_sequence, row_pooling_ratios=row_pooling_ratios, col_pooling_ratios=col_pooling_ratios)

# Example Usage:
orig_input = tf.constant([[[[1.0], [2.0], [3.0]], [[4.0], [5.0], [6.0]], [[7.0], [8.0], [9.0]]]])
orig_pool = tf.constant([[2, 2]])
orig_output = tf.raw_ops.fractional_max_pool(orig_input, pooling_ratio=[1.0, 1.0, 2.0, 2.0], pseudo_random=True)
grad = tf.constant([[[[1.0], [2.0]], [[3.0], [4.0]]]])
row_pooling_sequence = tf.raw_ops.fractional_max_pool_v2(orig_input, pooling_ratio=[1.0, 1.0, 1.0, 1.0], seed=0, seed2=0)[0]
col_pooling_sequence = tf.raw_ops.fractional_max_pool_v3(orig_input, pooling_ratio=[1.0, 1.0, 1.0, 1.0], seed=0, seed2=0)[1]
row_pooling_ratios = [0.5, 0.5]
col_pooling_ratios = [0.5, 0.5]

gradient = compute_fractional_max_pool_gradient(orig_input, orig_pool, orig_output, grad, row_pooling_sequence, col_pooling_sequence, row_pooling_ratios, col_pooling_ratios)
print("FractionalMaxPool Gradient:")
print(gradient)
