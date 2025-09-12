import tensorflow as tf

def fractional_avg_pool_grad(orig_pool, grad_output, seed0, seed1):
    grad_input = tf.raw_ops.FractionalMaxPoolGradV2(orig_pool=orig_pool,
                                                   grad=grad_output,
                                                   random_seed0=seed0,
                                                   random_seed1=seed1)
    return grad_input
