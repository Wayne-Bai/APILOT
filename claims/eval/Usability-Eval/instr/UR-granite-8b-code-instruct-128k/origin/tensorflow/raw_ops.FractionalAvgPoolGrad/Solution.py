import tensorflow as tf

# Define the FractionalAvgPool function
def FractionalAvgPool(value, pooling_ratio, pseudo_random=True, overlapping=False,
 deterministic=False, seed=0, seed2=0, name=None):
 return tf.raw_ops.FractionalAvgPool(value=value, pooling_ratio=pooling_ratio,
 pseudo_random=pseudo_random, overlapping=overlapping, deterministic=deterministic,
 seed=seed, seed2=seed2, name=name)

# Define the FractionalAvgPoolGrad function
def FractionalAvgPoolGrad(orig_input_shape, grad, block_size, name=None):
 return tf.raw_ops.FractionalAvgPoolGrad(orig_input_shape=orig_input_shape,
 grad=grad, block_size=block_size, name=name)

# Define the constant function
def constant(shape, dtype=tf.float32, name=None):
 return tf.raw_ops.Const(shape=shape, dtype=dtype, value=0, name=name)