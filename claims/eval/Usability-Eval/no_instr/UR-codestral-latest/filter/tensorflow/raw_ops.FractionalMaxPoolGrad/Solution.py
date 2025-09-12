import tensorflow as tf

# Define a function for the FractionalMaxPool operation
def frax_max_pool(x, pooling_ratio):
    return tf.raw_ops.FractionalMaxPool(
        value=x, pooling_region=tf.ones_like(x), pseudorandom=False,
        overlapping=False, deterministic=True, seed=0, seed2=0,
        pooling_ratio=[1, pooling_ratio, pooling_ratio, 1],
    )

# Define a function for the gradient operation
def grad_frax_max_pool(x, pooling_ratio):
    # Compute the frax_max_pool and its gradient
    y, grad = tf.raw_ops.FractionalMaxPoolGrad(
        orig_input=x, out_backprop=tf.ones_like(x), output=frax_max_pool(x, pooling_ratio),
        overlap=tf.zeros_like(x), out_batch=tf.shape(x)[0:1], out_height=tf.shape(x)[1:2],
        out_width=tf.shape(x)[2:3], out_channels=tf.shape(x)[3:4],
        pooling_region=tf.ones_like(x), row_pooling_sequence=tf.zeros_like(x),
        col_pooling_sequence=tf.zeros_like(x), pseudorandom=False,
        overlapping=False, deterministic=True, seed=0, seed2=0,
        pooling_ratio=[1, pooling_ratio, pooling_ratio, 1],
    )
    return grad
