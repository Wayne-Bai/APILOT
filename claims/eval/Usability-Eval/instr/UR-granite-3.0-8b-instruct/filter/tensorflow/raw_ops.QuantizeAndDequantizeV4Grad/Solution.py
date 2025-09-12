import tensorflow as tf

# Define a custom gradient for QuantizeAndDequantizeV4
@tf.custom_gradient
def quantize_and_dequantize_v4(input_tensor, min_range, max_range, narrow_range):
    output_tensor = tf.raw_ops.QuantizeAndDequantizeV4(
        input_tensor=input_tensor,
        min_range=min_range,
        max_range=max_range,
        narrow_range=narrow_range
    )
    def grad_fn(grad_output):
        # Compute the gradient of the QuantizeAndDequantizeV4 operation
        # This is a placeholder for the actual gradient computation
        # You need to replace it with the actual gradient computation logic
        return grad_output * 2  # Placeholder gradient computation

    return output_tensor, grad_fn

# Example usage
input_tensor = tf.constant([1.0, 2.0, 3.0], dtype=tf.float32)
min_range = tf.constant(0.0, dtype=tf.float32)
max_range = tf.constant(255.0, dtype=tf.float32)
narrow_range = tf.constant(True, dtype=tf.bool)

quantized_tensor = quantize_and_dequantize_v4(input_tensor, min_range, max_range, narrow_range)
grad_output = tf.constant([1.0, 2.0, 3.0], dtype=tf.float32)
grad_input = grad_fn(grad_output)

print("Quantized Tensor:", quantized_tensor.numpy())
print("Gradient Input:", grad_input.numpy())
