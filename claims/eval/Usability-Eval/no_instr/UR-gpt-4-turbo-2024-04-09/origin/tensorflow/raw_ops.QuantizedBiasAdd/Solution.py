import tensorflow as tf

def quantized_add(input_tensor, bias_tensor, min_input, max_input, min_bias, max_bias):
    # Adding the bias to the input tensor
    output, min_output, max_output = tf.raw_ops.QuantizedAdd(
        x=input_tensor, 
        y=bias_tensor,
        min_x=min_input,
        max_x=max_input,
        min_y=min_bias,
        max_y=max_bias
    )
    return output, min_output, max_output

# Example usage:
# Prepare quantized inputs and bias
input_tensor = tf.constant([10, 20, 30], dtype=tf.quint8)
bias_tensor = tf.constant([1, 1, 1], dtype=tf.quint8)
min_input = tf.constant([0], dtype=tf.float32) # minimum value of the input tensor
max_input = tf.constant([255], dtype=tf.float32) # maximum value of the input tensor
min_bias = tf.constant([0], dtype=tf.float32) # minimum value of the bias tensor
max_bias = tf.constant([255], dtype=tf.float32) # maximum value of the bias tensor

# Perform quantized addition
result, min_output, max_output = quantized_add(input_tensor, bias_tensor, min_input, max_input, min_bias, max_bias)
print("Quantized addition result:", result)
