import tensorflow as tf
from tensorflow.python.ops import array_ops

@tf.custom_gradient
def fractional_avg_pool(inputs):
    @tf.function
    def forward(inputs):
        return array_ops.fractional_avg_pool(
            inputs, ksize=3, strides=2, padding="SAME")

    @tf.function
    def grad(gradients, inputs):
        return tf.gradients(forward(inputs), inputs) * (1 - forward(inputs)) + \
                array_ops.fractional_avg_pool(gradients, ksize=3, strides=2, padding="SAME")

    return grad
