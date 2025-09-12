import tensorflow as tf

def add_bias(input_tensor, bias_tensor):
    return tf.raw_ops.AddV2(input=input_tensor, b=bias_tensor)

# Example usage
input_tensor = tf.constant([1.0, 2.0, 3.0], dtype=tf.quantized_float)
bias_tensor = tf.constant([0.5, 0.5, 0.5], dtype=tf.quantized_float)
result = add_bias(input_tensor, bias_tensor)
print(result)
