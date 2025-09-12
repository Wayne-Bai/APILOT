
import tensorflow as tf

@tf.custom_gradient
def custom_fractional_avg_pool_grad(grad, indices, kernel_shape, image_shape):
    def grad_fn(grad_upstream):
        return tf.raw_ops.FractionalAvgPoolGrad(grad_upstream, indices, kernel_shape=kernel_shape, image_shape=image_shape)
    return grad_fn

# Example parameters
grad = tf.constant(1.0)
indices = tf.constant([[1, 2], [3, 4]])
kernel_shape = [2, 2]
image_shape = [4, 4]

# Call the custom gradient function
result = custom_fractional_avg_pool_grad(grad, indices, kernel_shape, image_shape)

print(result)
