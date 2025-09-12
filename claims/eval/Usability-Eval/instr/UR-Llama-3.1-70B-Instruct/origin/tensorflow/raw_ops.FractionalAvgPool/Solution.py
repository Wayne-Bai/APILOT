import tensorflow as tf

# Create a 4-dimensional tensor as input
inputs = tf.random.uniform(shape=[1, 4, 4, 1], minval=0, maxval=10, dtype=tf.int32)

# Define the output size for fractional average pooling
output_size = [2, 2]  # Output size [H, W]

# Calculate the pooling ratio
pooling_ratio = [2, 2]  # Pooling ratio [H, W]

# Perform fractional average pooling
frac_avg_pooling = tf.raw_ops.FractionalAvgPool(
    value=inputs,
    pooling_ratio=pooling_ratio,
    pseudo_random=False,
    overlapping=False,
    deterministic=False,
    seed=0,
    seed2=0,
    output_shape=None,
)

with tf.Session() as sess:
    result = sess.run(frac_avg_pooling)
    print("Input:")
    print(sess.run(inputs))
    print("Output:")
    print(result)
