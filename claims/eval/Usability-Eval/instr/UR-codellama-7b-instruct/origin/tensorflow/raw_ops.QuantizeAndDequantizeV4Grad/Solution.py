
import tensorflow as tf

# Define input and output tensors for the QuantizeAndDequantizeV4 operation
input_tensor = tf.constant([1, 2, 3, 4, 5])
output_tensor = tf.quantization.QuantizeAndDequantizeV4(input_tensor)

# Get the gradient of the output tensor with respect to the input tensor
grad = tf.gradients(output_tensor, input_tensor)
