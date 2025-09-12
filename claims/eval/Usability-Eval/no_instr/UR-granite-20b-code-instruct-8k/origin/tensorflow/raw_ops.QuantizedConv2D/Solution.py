import tensorflow as tf

def compute_2d_convolution(input, filter):
  """
  Computes a 2D convolution given quantized 4D input and filter tensors.
  
  Args:
  input: A 4D tensor of shape `[batch, height, width, in_channels]` and type `quint8`.
  filter: A 4D tensor of shape `[filter_height, filter_width, in_channels, out_channels]` and type `quint8`.
  
  Returns:
  A 4D tensor of shape `[batch, out_height, out_width, out_channels]` and type `qint32`.
  """
  return tf.raw_ops.QuantizedConv2D(input=input, filter=filter, strides=[1, 1, 1, 1], padding="SAME")
