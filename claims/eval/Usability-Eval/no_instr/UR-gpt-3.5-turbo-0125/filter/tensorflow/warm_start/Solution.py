
import tensorflow as tf

dataset = tf.data.Dataset.range(10)

# Create an iterator with prefetching in the background
iterator = dataset.prefetch(buffer_size=tf.data.experimental.AUTOTUNE)

# Generate elements using the iterator
for element in iterator:
    print(element)
