import tensorflow as tf

# Define a user-defined function that takes inputs and provides the required Real-valued fast Fourier transform
def fft_1d(inputs):
  real_input = tf.real(inputs)
  imag_input = tf.imag(inputs)
  zeroth_order_coeff = tf.zeros((inputs.shape[0], inputs.shape[1]), dtype=inputs.dtype)
  vec = tf.concat([zeroth_order_coeff, tf.tensordot(real_input, tf.range(1, inputs.shape[1] + 1)), tf.tensordot(imag_input, tf.range(1, inputs.shape[1] + 1))], 1)
  zeros = tf.zeros((inputs.shape[0], 1 - inputs.shape[1] % 2), dtype=inputs.dtype)
  vec = tf.concat([zeros, vec, zeros], 1)
  return tf.tensordot(vec, vec, axes=([1, 2], [1, 2]), name=tf.raw_ops.MatrixPower_1)
