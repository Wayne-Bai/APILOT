import tensorflow as tf

# Define the inputs and attributes of the FractionalAvgPool function
value = tf.placeholder(tf.float32, shape=[None, None, None, None])
pooling_ratio = tf.placeholder(tf.float32, shape=[None, 1])
pseudo_random = tf.placeholder(tf.bool, shape=[])
overlapping = tf.placeholder(tf.bool, shape=[])
deterministic = tf.placeholder(tf.bool, shape=[])
seed = tf.placeholder(tf.int32, shape=[])
seed2 = tf.placeholder(tf.int32, shape=[])

# Compute the gradient of the FractionalAvgPool function
grad = tf.raw_ops.FractionalAvgPoolGrad(
    orig_input=value,
    orig_output=value,
    out_backprop=value,
    pooling_ratio=pooling_ratio,
    pseudo_random=pseudo_random,
    overlapping=overlapping,
    deterministic=deterministic,
    seed=seed,
    seed2=seed2
)
