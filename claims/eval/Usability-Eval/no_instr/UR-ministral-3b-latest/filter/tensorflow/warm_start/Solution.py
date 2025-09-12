import tensorflow as tf

# Example of using the `tf.data()` API to prefetch data, ensuring that elements are
# prefetched asynchronously when the iterator "futures" are requested at construct time.
batch_size = 32

# Create a `tf.data.Dataset` object
dataset = tf.data.Dataset.range(10000).batch(batch_size)

# Prefetch a fixed number of elements (for example, 32 elements)
dataset = dataset.prefetch(buffer_size=32)
