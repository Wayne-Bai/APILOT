import tensorflow as tf

# Create a dataset from a list of integers
dataset = tf.data.Dataset.from_tensor_slices([1, 2, 3, 4, 5])

# Iterate over the dataset and print the elements
for element in dataset:
    print(element.numpy())
