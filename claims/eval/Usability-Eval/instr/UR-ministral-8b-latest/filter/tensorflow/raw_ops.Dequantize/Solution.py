import tensorflow as tf

def dequantize_tensor(input_tensor):
    # Ensure the input_tensor is a quantized tensor
    if not hasattr(input_tensor, 'shape'):
        raise ValueError("Input tensor must be a quantized tensor")

    # Convert quantized tensor to float or bfloat16 tensor
    dequantized_tensor = tf.raw_ops.Dequantize(input_tensor, mind_ref=0.0, max_ref=1.0)
    return dequantized_tensor

# Example usage:
quantized_tensor = tf.constant([0, 127, 255], dtype=tf.int8)  # Example quantized tensor
dequantized_tensor = dequantize_tensor(quantized_tensor)
print(dequantized_tensor)
