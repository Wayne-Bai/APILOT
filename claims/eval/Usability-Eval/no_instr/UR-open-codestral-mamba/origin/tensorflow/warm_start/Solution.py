import tensorflow as tf

# Create a simple dataset
dataset = tf.data.Dataset.from_tensor_slices(tf.data.Dataset.range(10))

# Use the prefetch transformation
autotuned = tf.data.AUTOTUNE
dataset = dataset.prefetch(autotuned)

# Create an iterator
iterator = iter(dataset)

# Print the next element from the iterator
print(next(iterator))
