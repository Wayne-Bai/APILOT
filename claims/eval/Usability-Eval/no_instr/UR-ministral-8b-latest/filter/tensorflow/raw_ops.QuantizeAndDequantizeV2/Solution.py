import tensorflow as tf

def quantize_tf(tensor):
    # Adds a scale and zero_point to the tensor for quantization
    def quantize_tf(tensor, scale=128, zero_point=128):
        quantized_tensor = tf.derived_tensor(
            tensor,
            tf.raw_ops.Quantize(
                api_version=4,
                input=tensor,
                scale=scale,
                zero_point=zero_point
            )
        )
        return quantized_tensor

    def dequantize_tf(quantized_tensor, scale=128, zero_point=128):
        dequantized_tensor = tf.raw_ops.Dequantize(
            api_version=4,
            input=quantized_tensor,
            out_dtype=tf.float32
        )
        return dequantized_tensor

    quantized = quantize_tf(tensor)
    dequantized = dequantize_tf(quantized)

    return dequantized

# Example usage
tensor = tf.constant([1.0, 1.1, 1.2], dtype=tf.float32)
quantized_dequantized = quantize_tf(tensor)
print(quantized_dequantized)
