import tensorflow as tf

# Create a placeholder for the input tensor
input_tensor = tf.placeholder(tf.uint8, shape=[None, None, None], name='input')

# Create a placeholder for the scale and zero_point values
scale = tf.placeholder(tf.float32, shape=[], name='scale')
zero_point = tf.placeholder(tf.uint8, shape=[], name='zero_point')

# Use tf.raw_ops.Dequantize to dequantize the input tensor
dequantized_tensor = tf.raw_ops.Dequantize(input=input_tensor, scale=scale, zero_point=zero_point, dtype=tf.float32)

# Create a session to run the graph
with tf.Session() as sess:
    # Run the session with actual input values to get the dequantized tensor
    dequantized_output = sess.run(dequantized_tensor, feed_dict={
        input_tensor: [[[1, 2], [3, 4]], [[5, 6], [7, 8]]],
        scale: 0.5,
        zero_point: 127
    })

# Print the dequantized output
print(dequantized_output)
