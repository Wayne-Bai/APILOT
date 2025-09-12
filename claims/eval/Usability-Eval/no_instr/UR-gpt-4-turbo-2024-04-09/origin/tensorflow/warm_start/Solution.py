import tensorflow as tf

# Create a dataset
dataset = tf.data.Dataset.range(10)

# Configure the dataset to prefetch elements
# Set `start_background_threads` to True to start prefetching upon iterator creation
dataset = dataset.prefetch(buffer_size=tf.data.AUTOTUNE, start_background_threads=True)

# Create an iterator from the dataset
iterator = iter(dataset)

# Retrieve elements from the iterator
for item in iterator:
    print(item)
