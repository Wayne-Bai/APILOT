import tensorflow as tf

# Define input tensors
input_tensor = tf.placeholder(dtype=tf.float32, shape=[None, None, None, 1], name='input')
output_tensor = tf.placeholder(dtype=tf.float32, shape=[None, None, None, 1], name='output')

# Compute gradients
grads = tf.raw_ops.MaxPoolGrad(
    input=input_tensor,
    output=output_tensor,
    ksize=[1, 2, 2, 1],  # kernel size
    strides=[1, 2, 2, 1],  # stride
    padding='SAME'
)

# Define session and run computation
sess = tf.Session()
result = sess.run(grads, feed_dict={input_tensor: input_data})

print(result)
