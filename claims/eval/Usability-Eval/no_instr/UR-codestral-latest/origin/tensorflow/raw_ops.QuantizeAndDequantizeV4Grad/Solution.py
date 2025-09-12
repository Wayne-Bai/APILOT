import tensorflow as tf
from tensorflow.python.framework import ops
from tensorflow.python.ops import array_ops
from tensorflow.python.ops import gradients_impl

# Define a constant tensor
input_tensor = tf.constant([1.0, 2.0, 3.0], dtype=tf.float32)

# Define a custom gradient for QuantizeAndDequantizeV4
@ops.RegisterGradient("QuantizeAndDequantizeV4")
def _quantize_and_dequantize_v4_grad(op, *grads):
    return gradients_impl.identity_grad(op.inputs[0], grads[0])

# Add the QuantizeAndDequantizeV4 operation to the graph
quantized = tf.raw_ops.QuantizeAndDequantizeV4(input=input_tensor, min_range=-10.0, max_range=10.0, Tinput=tf.float32, Toutput=tf.float32)

# Define a loss function
loss = tf.reduce_sum(quantized)

# Compute the gradient of the loss with respect to the input_tensor
grads = tf.gradients(loss, input_tensor)

# Run the graph in a session
with tf.Session() as sess:
    grads_val = sess.run(grads, feed_dict={input_tensor: [1.0, 2.0, 3.0]})
    print(grads_val)
