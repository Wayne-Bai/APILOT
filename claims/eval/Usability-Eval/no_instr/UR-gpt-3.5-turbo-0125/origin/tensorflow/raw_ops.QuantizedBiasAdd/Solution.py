
import tensorflow as tf

def add_quantized_bias(input_tensor, bias_tensor):
    return tf.raw_ops.QuantizedAdd(input=input_tensor, bias=bias_tensor)

# Example usage
input_tensor = tf.constant([1, 2, 3], dtype=tf.quint8)
bias_tensor = tf.constant([0, 0, 1], dtype=tf.qint8)
output = add_quantized_bias(input_tensor, bias_tensor)

print(output)
