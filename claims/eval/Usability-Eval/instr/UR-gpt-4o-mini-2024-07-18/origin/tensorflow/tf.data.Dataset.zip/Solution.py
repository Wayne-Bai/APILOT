import tensorflow as tf

# Sample datasets
dataset1 = tf.data.Dataset.from_tensor_slices([1, 2, 3])
dataset2 = tf.data.Dataset.from_tensor_slices(['a', 'b', 'c'])

# Zipping the datasets together
zipped_dataset = tf.data.Dataset.zip((dataset1, dataset2))

# Iterate through the combined dataset and print each element
for element in zipped_dataset:
    print(element)
