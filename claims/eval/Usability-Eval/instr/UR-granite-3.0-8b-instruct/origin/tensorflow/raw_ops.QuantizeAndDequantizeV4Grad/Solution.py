import tensorflow as tf

# Define the input tensor
input_tensor = tf.constant([1.0, 2.0, 3.0, 4.0, 5.0])

# Define the quantization parameters
quantization_parameters = tf.constant([0.5, 0.5])

# Define the quantize and dequantize operation
quantized_tensor = tf.raw_ops.QuantizeAndDequantizeV4(
    input_tensor,
    quantization_parameters[0],
    quantization_parameters[1],
    narrow_range=True
)

# Define the gradient of the quantize and dequantize operation
gradient = tf.gradients(quantized_tensor, input_tensor)[0]

print(gradient)
