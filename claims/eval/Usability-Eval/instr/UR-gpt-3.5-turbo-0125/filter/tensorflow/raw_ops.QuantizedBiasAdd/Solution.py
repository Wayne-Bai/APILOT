
import tensorflow as tf

input_tensor = tf.placeholder(tf.int8, shape=[None, 224, 224, 3])
bias_tensor = tf.placeholder(tf.int8, shape=[3])

output_tensor = tf.raw_ops.QuantizedBiasAdd(input=input_tensor, bias=bias_tensor)

with tf.Session() as sess:
    result = sess.run(output_tensor, feed_dict={input_tensor: your_input_data, bias_tensor: your_bias_data})
