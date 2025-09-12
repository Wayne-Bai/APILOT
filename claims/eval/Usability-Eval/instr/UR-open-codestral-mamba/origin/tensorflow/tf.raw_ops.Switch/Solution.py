import tensorflow as tf

def conditional_forwarding(input_tensor, pred):
    output_tensor = tf.compat.v1.raw_ops.Switch(data=input_tensor, pred=pred, name=None)
    return output_tensor

# Placeholder for input tensor and predicate tensor
input_tensor = tf.placeholder(tf.float32, shape=[None], name='input_tensor')
predicate_tensor = tf.placeholder(tf.bool, shape=[], name='predicate_tensor')

# Use the conditional_forwarding function
output_tensor = conditional_forwarding(input_tensor, predicate_tensor)

# Initialize the TensorFlow session and run the operation
with tf.Session() as sess:
    output = sess.run(output_tensor, feed_dict={input_tensor: [1.0, 2.0, 3.0], predicate_tensor: True})
    print(output)
