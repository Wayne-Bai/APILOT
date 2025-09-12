import tensorflow as tf

def FractionalAvgPool_grad(orig_input, orig_output, out_backprop):
    # Compute gradient of the FractionalAvgPool function
    grad = tf.raw_ops.FractionalAvgPoolGrad(orig_input=orig_input, orig_output=orig_output, out_backprop=out_backprop)
    return grad
