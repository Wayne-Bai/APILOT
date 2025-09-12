import tensorflow as tf

# Create a TensorFlow session to execute operations
tf.config.experimental_run_functions_eagerly(True)

# Create a sample tensor
original_tensor = tf.constant([[1.0, 2.5, 3.1], [4.8, 5.5, 6.9]], dtype=tf.float32)

# Set quantization parameters
min_value = 0.0
max_value = 10.0
num_bits = 8

# Quantize the tensor
quantized_tensor = tf.quantization.quantize_and_dequantize(
    original_tensor,
    input_min=min_value,
    input_max=max_value,
    num_bits=num_bits,
    signed_input=True,
    range_given=True
)

# Initialize a session and run the operation
tf.print("Original Tensor:", original_tensor)
tf.print("Quantized and Dequantized Tensor:", quantized_tensor)
