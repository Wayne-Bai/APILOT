import tensorflow as tf

# Create a TensorFlow dataset
dataset = tf.data.Dataset.range(100)

# Enable background threads for asynchronous transformations
dataset = dataset.prefetch(buffer_size=tf.data.experimental.AUTOTUNE)

# Create an iterator for the dataset
iterator = dataset.as_numpy_iterator()

# Iterate through the dataset
for element in iterator:
    print(element)
