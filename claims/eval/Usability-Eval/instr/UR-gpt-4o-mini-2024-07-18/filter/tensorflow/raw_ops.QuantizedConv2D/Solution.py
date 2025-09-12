import tensorflow as tf

def quantized_2d_convolution(input_tensor, filters, bias, strides, padding, quant_min, quant_max):
    # Performing quantized 2D convolution
    # Cast inputs to tf.int8 if they are not already
    input_tensor = tf.cast(input_tensor, tf.int8)
    filters = tf.cast(filters, tf.int8)
    bias = tf.cast(bias, tf.int32)

    # Using tf.nn.quantized_conv2d
    output = tf.nn.quantized_conv2d(
        input=input_tensor,
        filters=filters,
        bias=bias,
        strides=strides,
        padding=padding,
        activation_min=quant_min,
        activation_max=quant_max
    )
    
    return output
