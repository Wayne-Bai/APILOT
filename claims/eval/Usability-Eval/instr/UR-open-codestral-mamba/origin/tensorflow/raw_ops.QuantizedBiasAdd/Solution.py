import tensorflow as tf

# Define a simple Quantized add operation
def quantized_add(input, bias):
    return tf.raw_ops.AddV2(input=input, y=bias)

# Create a sample input and bias tensor
input = tf.constant([1, 2, 3, 4, 5], dtype=tf.qint8)
bias = tf.constant([1, 2, 3, 4, 5], dtype=tf.qint8)

# Use the function to add the bias to the input
result = quantized_add(input, bias)

print("Input: ", input.numpy())
print("Bias: ", bias.numpy())
print("Result: ", result.numpy())
