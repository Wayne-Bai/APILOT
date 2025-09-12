import tensorflow as tf

# Create a sequence of numbers
sequence = tf.data.Dataset.from_tensor_slices(tf.range(100))
print(sequence)
