
import tensorflow as tf

@tf.custom_gradient
def fractional_avg_pool_grad(orig_input_tensor, pooling_ratio, pseudo_random, overlapping, deterministic):
    def grad(dy):
        return tf.raw_ops.FractionalAvgPoolGrad(dy, orig_input_tensor, pooling_ratio=pooling_ratio, pseudo_random=pseudo_random, overlapping=overlapping, deterministic=deterministic)
    
    return grad

# Call the gradient function with required parameters
output_grad_func = fractional_avg_pool_grad(orig_input_tensor, pooling_ratio=[2.0, 2.0], pseudo_random=False, overlapping=False, deterministic=True)
