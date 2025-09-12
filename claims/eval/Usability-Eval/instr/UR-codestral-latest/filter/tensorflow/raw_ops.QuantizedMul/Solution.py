import tensorflow as tf

def quantized_mult(x, y, min_x, max_x, min_y, max_y, min_out, max_out):
    # Define QuantizationConfigs
    quant_config_x = tf.raw_ops.QuantizationConfig(
        is_signed=False,  # Update as needed based on your data
        num_bits=8,
        exponent=-127,  # Update as needed based on your data
        min=min_x,
        max=max_x,
        output_min=min_out,
        output_max=max_out)

    quant_config_y = tf.raw_ops.QuantizationConfig(
        is_signed=False,  # Update as needed based on your data
        num_bits=8,
        exponent=-127,  # Update as needed based on your data
        min=min_y,
        max=max_y,
        output_min=min_out,
        output_max=max_out)

    # Quantize the tensors
    x_quantized = tf.quantization.fake_quant_with_min_max_args(
        x, min=min_x, max=max_x, num_bits=8)

    y_quantized = tf.quantization.fake_quant_with_min_max_args(
        y, min=min_y, max=max_y, num_bits=8)

    # Perform the quantized multiplication
    out_quantized = tf.raw_ops.QuantizedMul(x=x_quantized, y=y_quantized, Toutput=tf.quint8,
                                            min_x=min_x, max_x=max_x, min_y=min_y, max_y=max_y,
                                            min_output=min_out, max_output=max_out, output_min=min_out, output_max=max_out,
                                            input_quant_mode='MIN_FIRST', output_quant_mode='MIN_FIRST')

    return out_quantized
