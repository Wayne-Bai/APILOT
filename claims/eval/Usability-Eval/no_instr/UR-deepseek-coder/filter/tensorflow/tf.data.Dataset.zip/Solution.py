import tensorflow as tf

# Example datasets
dataset1 = tf.data.Dataset.from_tensor_slices([1, 2, 3, 4, 5])
dataset2 = tf.data.Dataset.from_tensor_slices(["a", "b", "c", "d", "e"])

# Zip the datasets together
zipped_dataset = tf.data.Dataset.zip((dataset1, dataset2))

# Iterate through the zipped dataset to see the result
for element in zipped_dataset:
    print(element)
