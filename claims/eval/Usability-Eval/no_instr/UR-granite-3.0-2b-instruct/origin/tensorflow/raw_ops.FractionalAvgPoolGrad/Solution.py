import tensorflow as tf

# Define the FractionalAvgPool function
def fractional_avg_pool(input, fractional_pooling_ratio):
    pool_size = int(input.shape[1] * fractional_pooling_ratio)
    output = tf.raw_ops.FractionalAvgPool(input, pool_size, strides=1, padding='SAME')
    return output

# Compute gradient of the FractionalAvgPool function
def compute_gradient(input, output, fractional_pooling_ratio):
    with tf.GradientTape() as tape:
        tape.watch(input)
        output = fractional_avg_pool(input, fractional_pooling_ratio)
        loss = tf.reduce_mean(output)
    grads = tape.gradient(loss, input)
    return grads
