import tensorflow as tf

def quantized_conv2d(input_quantized, filter_quantized):
    with tf.raw_ops.conv2d(
        input=input_quantized,
        filters=filter_quantized,
        strides=[1, 1],
        padding="VALID",
        use_cudnn_on_gpu=True,
        name='QuantizedConv2D'
    ) as output_quantized:
        return output_quantized

# Example usage:
input_quantized = tf.quantized.fake_quant_with_min_max_observer(tf.rand(1, 28, 28, 3), -127, 128, -127, 128)
filter_quantized = tf.quantized.fake_quant_with_min_max_observer(tf.rand(1, 3, 3, 32), -127, 128, -127, 128)
output_quantized = quantized_conv2d(input_quantized, filter_quantized)
print(output_quantized)
