import tensorflow as tf

# Define the FractionalMaxPoolGrad function
def FractionalMaxPoolGrad(grad_y, grad_x, input_y, input_x, fraction):
    # Calculate the gradient of the input with respect to the output
    grad_input_y = tf.raw_ops.FractionalMaxPoolGrad(grad_y, grad_x, input_y, input_x, fraction)

    return grad_input_y
