
import tensorflow as tf

def add_quantized_bias(input, bias):
    # Add bias to input for quantized types
    return tf.raw_ops.QuantizedAdd(input=input, bias=bias)

# Usage example
input_tensor = tf.constant([[1, 2], [3, 4]], dtype=tf.dtypes.int8)
bias_tensor = tf.constant([[0, 0], [1, 1]], dtype=tf.dtypes.int8)
output = add_quantized_bias(input=input_tensor, bias=bias_tensor)

print(output)
