
import tensorflow as tf

# Here you can start using the tf.data module from TensorFlow 2.x onwards
# For example, you can use tf.data.Dataset to create a dataset from a list
dataset = tf.data.Dataset.from_tensor_slices([1, 2, 3, 4, 5])

# You can also apply transformations to the dataset
dataset = dataset.map(lambda x: x * 2)

# Iterate through the dataset and print the elements
for element in dataset:
    print(element)
