import tensorflow as tf

# Creating a dataset
dataset = tf.data.Dataset.range(10)

# Using prefetch to improve the latency of the first 'next()' calls at the cost of using more memory
dataset = dataset.prefetch(buffer_size=tf.data.experimental.AUTOTUNE)

# Iterating over the dataset
for item in dataset:
    # Perform your asynchronous transformations here
    print(item.numpy())
