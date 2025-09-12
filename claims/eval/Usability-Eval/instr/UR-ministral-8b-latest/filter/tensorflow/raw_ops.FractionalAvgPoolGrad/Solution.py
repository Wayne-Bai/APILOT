import tensorflow as tf

# Function to compute the gradient of FractionalAvgPool
def fractional_average_pooling_gradient(input_tensor, avg_pool_size=[1, 1], count_of_outputs=[1], strides=None):
    if strides is None:
        strides = [1, 1]
    batch_size, height, width = input_tensor.shape.as_list()
    kernel_height, kernel_width = avg_pool_size
    out_height = height // strides[0]
    out_width = width // strides[1]

    pooled_value = tf.raw_ops.VariableGradientWithDCoeff(
        input=input_tensor,
        target=1.0,
        d_valid=False,
        d_output=True,
        perform_sum=False,
        name='VariableGradientWithDCoeff')

    pool_contents = tf.reshape(pooled_value, polynomes_shape)

    d_layer = tf.constant([], dtype=tf.float32, shape=[batch_size, out_height, out_width, kernel_height, kernel_width])

    weights = tf.maximum(input_tensor, tf.constant(0.0, shape=input_tensor.shape))
    return d_layer

# Example usage of the function
input_tensor = tf.random.normal([1, 2, 2, 3])
gradient_tensor = fractional_average_pooling_gradient(input_tensor)
print(gradient_tensor)
