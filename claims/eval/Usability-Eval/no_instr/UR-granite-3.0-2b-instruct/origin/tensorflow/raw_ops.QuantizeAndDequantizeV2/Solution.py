import tensorflow as tf

# Define the input tensor
input_tensor = tf.constant([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]], dtype=tf.float32)

# Define the quantization parameters
quantization_params = {
    "scale": tf.constant([0.5, 0.5, 0.5], dtype=tf.float32),
    "zero_point": tf.constant([0], dtype=tf.int32),
}

# Quantize the input tensor
quantized_tensor = tf.raw_ops.Quantize(
    input=input_tensor,
    quantization_params=quantization_params,
    output_type=tf.qint8,
)

# Dequantize the quantized tensor
dequantized_tensor = tf.raw_ops.Dequantize(
    input=quantized_tensor,
    dequantization_params={
        "scale": tf.constant([2.0, 2.0, 2.0], dtype=tf.float32),
        "zero_point": tf.constant([0], dtype=tf.int32),
    },
    output_type=tf.float32,
)

# Print the original, quantized, and dequantized tensors
print("Original tensor:")
print(input_tensor)
print("\nQuantized tensor:")
print(quantized_tensor)
print("\nDequantized tensor:")
print(dequantized_tensor)
