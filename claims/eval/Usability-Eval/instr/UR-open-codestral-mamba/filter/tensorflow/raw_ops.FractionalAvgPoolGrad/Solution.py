import tensorflow as tf
from tensorflow.python.framework import ops
from tensorflow.python.ops import array_ops
from tensorflow.python.ops import random_ops

@ops.RegisterGradient("FractionalAvgPool")
def _fractional_avg_pool_grad(op, gradient):
    return [tf.zeros(array_ops.shape(op.inputs[0]))]

# Test the gradient function
x = random_ops.random_uniform([1, 5, 5, 1], dtype=tf.float32)
op = tf.nn.fractional_avg_pool(x, [1.0, 0.5], [1, 1], 'SAME')
y, _ = op
grads = tf.gradients(y, [x])
with tf.Session() as sess:
    print(sess.run(grads))
