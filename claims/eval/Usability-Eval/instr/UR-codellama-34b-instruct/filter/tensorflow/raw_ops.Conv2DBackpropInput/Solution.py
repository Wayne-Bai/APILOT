import tensorflow as tf

@tf.function
def conv2d_grad_input(inputs, filters, strides, padding):
    # Convert inputs and filters to Tensors if they are not already
    inputs = tf.convert_to_tensor(inputs)
    filters = tf.convert_to_tensor(filters)

    # Perform the convolution
    conv_output = tf.nn.conv2d(inputs, filters, strides=strides, padding=padding)

    # Compute the gradients of the output with respect to the input
    input_gradients = tf.gradients(ys=conv_output, xs=inputs)

    return input_gradients
