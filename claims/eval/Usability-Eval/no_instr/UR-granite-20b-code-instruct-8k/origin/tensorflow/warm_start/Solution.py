import tensorflow as tf

dataset = tf.data.Dataset.from_tensor_slices([1, 2, 3, 4, 5])
dataset = dataset.map(lambda x: x*2)

# Set up background threads for asynchronous transformations
dataset = dataset.prefetch(buffer_size=5)

for element in dataset:
  print(element.numpy())
