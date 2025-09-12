import tensorflow as tf

def add_bias_to_input(input_tensor, bias_tensor):
    output_tensor = tf.raw_ops.BiasAdd(value=input_tensor, bias=bias_tensor)
    return output_tensor
