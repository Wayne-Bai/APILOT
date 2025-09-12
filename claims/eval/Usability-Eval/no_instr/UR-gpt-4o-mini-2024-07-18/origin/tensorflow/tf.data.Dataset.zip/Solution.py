import tensorflow as tf

# Example datasets
dataset1 = tf.data.Dataset.from_tensor_slices([1, 2, 3, 4])
dataset2 = tf.data.Dataset.from_tensor_slices(['a', 'b', 'c', 'd'])

# Zipping the datasets together
zipped_dataset = tf.data.Dataset.zip((dataset1, dataset2))

# Iterating through the zipped dataset
for item in zipped_dataset:
    print(item.numpy())
