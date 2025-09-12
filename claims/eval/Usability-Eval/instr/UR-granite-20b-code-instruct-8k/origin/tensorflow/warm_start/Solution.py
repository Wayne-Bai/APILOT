import tensorflow as tf

dataset = tf.data.Dataset.range(100)

# Set the number of background threads to be used when calling next() on the iterator.
dataset = dataset.prefetch(buffer_size=tf.data.experimental.AUTOTUNE)

for element in dataset:
  print(element)
