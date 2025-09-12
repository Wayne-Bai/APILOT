import tensorflow as tf

# Define the input tensor
input_tensor = tf.cast(tf.range(0, 10), tf.quint8)

# Define the bias tensor
bias_tensor = tf.cast(tf.range(0, 10, dtype=tf.quint8), tf.quint8)

# Add bias to input tensor
result_tensors = tf.raw_ops.AddV2(x=input_tensor, y=bias_tensor)

with tf.Session() as sess:
    result = sess.run(result_tensors)
    print(result)
