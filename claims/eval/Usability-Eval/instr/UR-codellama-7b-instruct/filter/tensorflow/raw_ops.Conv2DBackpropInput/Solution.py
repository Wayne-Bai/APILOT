import tensorflow as tf

# Define the function that computes the convolution
def conv2d(input_tensor, kernel_tensor):
    return tf.raw_ops.Conv2D(
        input=input_tensor,
        filter=kernel_tensor,
        strides=[1, 1, 1, 1],
        padding='SAME'
    )

# Define the function that computes the gradient of the convolution with respect to the input
def conv2d_backprop_input(input_tensor, kernel_tensor, output_tensor):
    return tf.raw_ops.Conv2DBackPropInput(
        input=input_tensor,
        filter=kernel_tensor,
        out_backprop=output_tensor,
        strides=[1, 1, 1, 1],
        padding='SAME'
    )
