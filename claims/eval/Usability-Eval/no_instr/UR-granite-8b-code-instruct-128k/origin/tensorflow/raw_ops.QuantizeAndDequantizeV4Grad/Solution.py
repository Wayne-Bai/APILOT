import tensorflow as tf

# Define the inputs
input = tf.constant([0.2, 0.4, 0.6, 0.8])

# Define the QuantizeAndDequantizeV4 op
output = tf.raw_ops.QuantizeAndDequantizeV4(input=input, min_range=0, max_range=1, T=tf.float32)

# Print the output
print(output)
