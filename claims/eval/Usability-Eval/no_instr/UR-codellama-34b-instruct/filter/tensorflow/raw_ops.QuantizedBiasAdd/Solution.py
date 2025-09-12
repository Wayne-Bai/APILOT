import tensorflow as tf

# Create an input tensor of size (1, 2) and a bias tensor of size (2, 1)
input_tensor = tf.constant([[10, 20]], dtype=tf.float32)
bias_tensor = tf.constant([[1], [2]], dtype=tf.int8)

# Add the bias to the input tensor
result_tensor = tf.quantization.add(input_tensor, bias_tensor, name='bias_add')

print("Input tensor:", input_tensor.numpy())
print("Bias tensor:", bias_tensor.numpy())
print("Result tensor:", result_tensor.numpy())
