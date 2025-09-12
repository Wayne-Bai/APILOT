import tensorflow as tf

def maxpool_grad(input_tensor, output_tensor, kernel_size, strides):
    grad_vals = tf.raw_ops.MaxPoolGrad(
        orig_input=input_tensor,
        orig_output=output_tensor,
        ksize=kernel_size,
        strides=strides)
    return grad_vals
