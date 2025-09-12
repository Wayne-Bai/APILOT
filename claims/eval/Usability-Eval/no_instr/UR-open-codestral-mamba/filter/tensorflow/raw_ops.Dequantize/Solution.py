import tensorflow as tf

# Define a function to dequantize the input tensor

def dequantize_tensor(input_tensor):
    dequantized_tensor = tf.raw_ops.Dequantize(input=input_tensor)
    return dequantized_tensor

# Test the function with a sample tensor

sample_tensor = tf.constant([1, 2, 3, 4, 5], dtype=tf.qint8)
dequantized_tensor = dequantize_tensor(sample_tensor)
print(dequantized_tensor)
