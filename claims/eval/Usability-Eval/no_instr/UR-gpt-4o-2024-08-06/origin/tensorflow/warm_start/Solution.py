import tensorflow as tf

# Sample dataset for demonstration
dataset = tf.data.Dataset.range(10)

# Applying some transformations
dataset = dataset.map(lambda x: x * 2)
dataset = dataset.batch(2)

# Create an iterator from the dataset
iterator = iter(dataset)

# Prefetch data to improve latency at the expense of higher memory usage
dataset = dataset.prefetch(tf.data.AUTOTUNE)

# Print the elements in the dataset
for element in iterator:
    print(element.numpy())
