import tensorflow as tf

def QuantizedConv2D(input, filter, strides, padding, out_type):
  # Define the quantized convolution operation
  quantized_conv = tf.raw_ops.QuantizedConv2D(input=input,filter=filter,strides=strides,padding=padding,out_type=out_type)
  
  return quantized_conv
