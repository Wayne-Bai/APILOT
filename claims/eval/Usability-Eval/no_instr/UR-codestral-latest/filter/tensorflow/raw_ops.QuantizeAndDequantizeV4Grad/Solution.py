import tensorflow as tf

def quantize_and_dequantize(input_tensor, scale, zero_point):
    # Quantize the input tensor
    quantized_tensor = tf.quantization.fake_quant_with_min_max_vars(input_tensor, min=0.0, max=1.0)
    # Dequantize the tensor
    dequantized_tensor = scale * (quantized_tensor - zero_point)
    return dequantized_tensor

@tf.function
def compute_gradients(input_tensor, scale, zero_point):
    with tf.GradientTape() as tape:
        tape.watch(input_tensor)
        result = quantize_and_dequantize(input_tensor, scale, zero_point)
    grad = tape.gradient(result, input_tensor)
    return grad

# Test the function
input_tensor = tf.constant([[0.5, 1.0], [1.5, 2.0]], dtype=tf.float32)
scale = tf.constant(0.5, dtype=tf.float32)
zero_point = tf.constant(0, dtype=tf.int32)
grad = compute_gradients(input_tensor, scale, zero_point)
print(grad)
