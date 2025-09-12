import tensorflow as tf

def fractional_avg_pool(inputs, pool_ratio):
    # Define strides based on pooling rate
    strides = [1, int(pool_ratio), int(pool_ratio), 1]

    # Create a pooling layer
    pooled = tf.nn.avg_pool(inputs, ksize=[1, strides[1], strides[2], 1], strides=strides, padding='SAME')

    return pooled

def fractional_avg_pool_grad(orig_input, out_grad, pool_ratio):
    # Scaling the upsampled gradient to match the shape of original input
    scale = tf.constant(pool_ratio ** 2, dtype=out_grad.dtype)
    upsampled_grad = tf.image.resize(out_grad, size=(tf.shape(orig_input)[1], tf.shape(orig_input)[2]), method='nearest')
    fractional_grad = upsampled_grad / scale

    return fractional_grad
