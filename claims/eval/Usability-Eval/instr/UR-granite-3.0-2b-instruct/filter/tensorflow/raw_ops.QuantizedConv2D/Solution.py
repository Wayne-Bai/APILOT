import tensorflow as tf

class QuantizedConv2D(tf.raw_op.RawOp):
    def __init__(self, **kwargs):
        super(QuantizedConv2D, self).__init__(**kwargs)

    def compute(self, input_tensors, **kwargs):
        # Extract input tensors
        input_tensor_x = input_tensors[0]
        input_tensor_y = input_tensors[1]

        # Perform quantization on input tensors
        quantized_input_tensor_x = tf.raw_ops.quantize_and_dequantize(input_tensor_x, tf.int8)
        quantized_input_tensor_y = tf.raw_ops.quantize_and_dequantize(input_tensor_y, tf.int8)

        # Perform 2D convolution
        output_tensor = tf.raw_ops.conv2d(quantized_input_tensor_x, quantized_input_tensor_y, **kwargs)

        return [output_tensor]
