import tensorflow as tf

# Define the sequence length and the range of values
seq_length = 10
start = 1
stop = 11
step = 2

# Create a sequence tensor using the range function
seq_tensor = tf.range(start, stop, step)

# Reshape the tensor to have the desired length
seq_tensor = tf.reshape(seq_tensor, (seq_length,))

print(seq_tensor)
