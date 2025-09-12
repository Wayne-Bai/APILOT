import tensorflow as tf
from tensorflow.python.ops import gen_nn_ops

# Assuming input_value is the input tensor and output_grad is the gradient tensor
output_grad = tf.constant([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
input_value = tf.constant([[10, 11, 12], [13, 14, 15], [16, 17, 18]])

# Compute gradient of FractionalMaxPool function
grad, indices = gen_nn_ops.fractional_max_pool_grad(
    input_value, output_grad, 0.5, [1, 1, 1, 1], seed=0, name=None)

with tf.Session() as sess:
    print(sess.run(grad))
    print(sess.run(indices))
