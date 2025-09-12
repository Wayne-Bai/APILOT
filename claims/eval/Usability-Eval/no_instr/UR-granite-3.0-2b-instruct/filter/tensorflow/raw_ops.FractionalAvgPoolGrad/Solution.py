import tensorflow as tf

# Define the FractionalAvgPool gradient function
def fractional_avg_pool_gradient(input, output_grad, pool_size, strides):
    # Create a FractionalAvgPool op with the given parameters
    op = tf.raw_ops.FractionalAvgPool(
        input=input,
        pool_size=pool_size,
        strides=strides,
        data_format='NHWC',
        name='fractional_avg_pool'
    )

    # Compute the gradient with respect to the input
    input_grad = tf.raw_ops.Gradient(
        op=op,
        output_grad=output_grad,
        name='input_gradient'
    )

    return input_grad
