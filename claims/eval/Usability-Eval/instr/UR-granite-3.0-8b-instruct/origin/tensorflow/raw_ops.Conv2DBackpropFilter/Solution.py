import tensorflow as tf

def conv2d_backprop_filter(input, filters, conv_output_shape, strides, padding, data_format):
    return tf.raw_ops.Conv2DBackpropFilterV2(
        input=input,
        filters=filters,
        conv_output_shape=conv_output_shape,
        strides=strides,
        padding=padding,
        data_format=data_format
    )
