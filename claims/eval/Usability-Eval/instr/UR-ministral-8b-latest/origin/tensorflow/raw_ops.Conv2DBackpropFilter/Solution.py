import tensorflow as tf

# Define a function to compute the gradients of convolution with respect to the filter using tf.raw_ops

def compute_conv_gradients(model, input_tensor, filter_variables, filter_grads, dtype=tf.float32):
    input_shape = input_tensor.shape
    filter_shape = filter_variables.shape.as_list()[1:3]

    with tf.raw_ops.depth_mult.Conv2DBackpropInput(
        input=input_tensor,
        filters=filter_variables,
        strides=None,
        padding='SAME'
    ) as conv_grad_op:
        conv_grad_op_ch = tf.raw_ops.depth_mult.Conv2DBackpropInputCH(input=input_tensor, filter=filter_variables,
                                                                     strides=None, padding='SAME')

    return conv_grad_op_ch

# Example usage
input_tensor = tf.random.normal([1, 28, 28, 3])
filter_variables = tf.random.normal([3, 3, 3, 32])
input_shape = input_tensor.shape
filter_shape = filter_variables.shape.as_list()[1:3]

conv_grad = compute_conv_gradients(input_tensor, filter_variables, input_shape, filter_shape)
print(conv_grad)
