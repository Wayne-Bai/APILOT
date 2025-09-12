import tensorflow as tf

def quantize_and_dequantize_v3(input_tensor, scale_shift_cor):
    quantized_tensor = tf.raw_ops.QuantizeAndDequantizeV4(
        input=input_tensor,
        scale_shift_cor=scale_shift_cor,
        reorder_point=scale_shift_cor.shape[0]
    )
    return quantized_tensor

# Example usage
input_tensor = tf.constant([[1, 2, 3], [4, 5, 6]])
scale_shift_cor = tf.constant([[0.5, 0.25], [0.25, 0.125]])
quantized_dequantized_tensor = quantize_and_dequantize_v3(input_tensor, scale_shift_cor)
