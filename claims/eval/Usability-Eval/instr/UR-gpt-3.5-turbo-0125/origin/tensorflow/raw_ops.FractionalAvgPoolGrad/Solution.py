
import tensorflow as tf

@tf.RegisterGradient("FractionalAvgPool")
def _fractional_avg_pool_grad(op, grad):
    return tf.raw_ops.FractionalAvgPoolGrad(grad, op.inputs[0], op.inputs[1], op.inputs[2], op.inputs[3], op.inputs[4], op.inputs[5], op.inputs[6])

# Example usage
input_data = tf.placeholder(tf.float32)
output = tf.raw_ops.FractionalAvgPool(input_data, newsize=[5, 5])
gradients = tf.gradients(output, input_data)

with tf.Session() as sess:
    result = sess.run(gradients, feed_dict={input_data: your_input_data})
