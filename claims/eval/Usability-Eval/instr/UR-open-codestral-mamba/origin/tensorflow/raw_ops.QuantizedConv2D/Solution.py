import tensorflow as tf
from tensorflow.python.ops import math_ops

def quantized_2d_conv(input, filters, strides, padding):
    input = tf.convert_to_tensor(input)
    filters = tf.convert_to_tensor(filters)

    # Ensure tensor ranks are correct
    expected_ranks = [4, 4]
    if tf.compat.v1.rank(input) != expected_ranks[0] or tf.compat.v1.rank(filters) != expected_ranks[1]:
        raise ValueError(f"Expected rank of input tensor is {expected_ranks[0]} and filter tensor is {expected_ranks[1]}")

    # Perform 2D convolution operation
    strides = [1, strides, strides, 1]
    padding = padding.upper()
    result = tf.raw_ops.QuantizedConv2D(input=input, filter=filters, strides=strides, padding=padding)

    return result

# Test the function
# Assuming we have an input tensor of shape [1, 5, 5, 1] and filters tensor of shape [1, 2, 2, 1]
input_tensor = tf.constant([[[[1], [2], [3], [4], [5]],
                             [[6], [7], [8], [9], [10]],
                             [[11], [12], [13], [14], [15]],
                             [[16], [17], [18], [19], [20]],
                             [[21], [22], [23], [24], [25]]]], dtype=tf.float32)

phi_tensor = tf.constant([[[[1], [2]],
                           [[3], [4]]]], dtype=tf.float32)

output = quantized_2d_conv(input_tensor, phi_tensor, 1, 'SAME')
print(output)
