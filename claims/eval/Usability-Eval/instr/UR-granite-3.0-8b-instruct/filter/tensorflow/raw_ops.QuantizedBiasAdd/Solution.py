import tensorflow as tf

def add_bias_to_quantized_tensor(input, bias):
    # Ensure input and bias have the same data type
    input = tf.cast(input, bias.dtype)
    bias = tf.cast(bias, input.dtype)

    # Add bias to input
    result = tf.raw_ops.QuantizedAdd(input, bias)

    return result
