import tensorflow as tf

# Example dataset
dataset = tf.data.Dataset.range(10)

# Transform the dataset (e.g. map, batch, etc.)
transformed_dataset = dataset.map(lambda x: x * x)

# Enable prefetching to improve the latency of the initial 'next()' calls
prefetched_dataset = transformed_dataset.prefetch(buffer_size=tf.data.AUTOTUNE)

# Create an iterator that starts background threads upon creation
iterator = prefetched_dataset.as_numpy_iterator()

# Fetch first element from the iterator, which should be more responsive
first_element = next(iterator)
print(first_element)

# Fetch additional elements
for element in iterator:
    print(element)
