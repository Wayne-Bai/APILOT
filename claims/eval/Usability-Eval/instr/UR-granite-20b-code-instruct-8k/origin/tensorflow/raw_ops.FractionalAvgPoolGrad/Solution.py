import tensorflow as tf

# Define the FractionalAvgPool function
def fractional_avg_pool(input, pooling_ratio, pseudo_random=False, name=None):
    # Compute gradient of FractionalAvgPool function
    grad = tf.raw_ops.FractionalAvgPoolGrad(orig_input=input, orig_output=output, pooling_ratio=pooling_ratio, pseudo_random=pseudo_random, name=name)
    
    return grad
