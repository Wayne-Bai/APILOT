import tensorflow as tf

# Create a dataset
dataset = tf.data.Dataset.range(10)

# Apply transformations (e.g., batching)
dataset = dataset.batch(2)

# Use the `prefetch` transformation to start background threads
# and specify a buffer size; setting it to tf.data.AUTOTUNE lets TensorFlow decide the optimal buffer size
dataset = dataset.prefetch(buffer_size=tf.data.AUTOTUNE)

# Create an iterator
iterator = iter(dataset)

# Fetch elements
for element in iterator:
    print(element)
