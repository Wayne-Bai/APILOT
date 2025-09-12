
import tensorflow as tf

# Define input tensor (4D tensor with shape [batch, height, width, channels])
input_tensor = tf.placeholder(tf.float32, shape=[None, height, width, channels])

# Define pooling window size (2x2 window with vertical and horizontal stride of 2)
pool_size = [1, 2, 2, 1]
strides = [1, 2, 2, 1]

# Perform fractional average pooling
output = tf.raw_ops.FractionalAvgPool(input=input_tensor, pooling_ratio=[1.0, 1.44, 1.44, 1.0], pseudo_random=False, overlapping=True, deterministic=False, seed=0, seed2=0, seed_generator="philox")

# Output tensor after fractional average pooling
output_tensor = output.output

# Run session to execute the fractional average pooling operation
with tf.Session() as sess:
    result = sess.run(output_tensor, feed_dict={input_tensor: input_data})
