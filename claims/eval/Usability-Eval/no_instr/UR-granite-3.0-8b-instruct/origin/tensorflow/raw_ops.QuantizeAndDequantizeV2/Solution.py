import tensorflow as tf

# Create a tensor
tensor = tf.constant([1.2, 3.5, 4.8, 5.1])

# Quantize the tensor
quantized_tensor = tf.raw_ops.QuantizeV2(
    input=tensor,
    min=0.0,
    max=10.0,
    num_bits=8,
    narrow_range=False
)

# Dequantize the tensor
dequantized_tensor = tf.raw_ops.Dequantize(
    input=quantized_tensor,
    min=0.0,
    max=10.0,
    num_bits=8,
    narrow_range=False
)

# Print the original, quantized, and dequantized tensors
print("Original Tensor: ", tensor.numpy())
print("Quantized Tensor: ", quantized_tensor.numpy())
print("Dequantized Tensor: ", dequantized_tensor.numpy())
