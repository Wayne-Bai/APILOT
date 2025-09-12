import tensorflow as tf

def fractional_avg_pool_grad(orig_input, grad, ksize, strides, padding='VALID'):
  output_shape = tf.shape(orig_input)
  new_grad = tf.raw_ops.FractionalAvgPoolGrad(orig_input_shape=output_shape,
                                               out_backprop=grad,
                                               roi=ksize,
                                               strides=strides,
                                               padding=padding)
  return new_grad
