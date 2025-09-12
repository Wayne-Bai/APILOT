import tensorflow as tf

# Create some example data
data = tf.constant([[1, 2], [3, 4], [5, 6], [7, 8]])

# TensorFlow's Dataset API can be used to shuffle the data
dataset = tf.data.Dataset.from_tensor_slices(data)

# Shuffle the dataset
shuffled_dataset = dataset.shuffle(buffer_size=len(data), seed=42)

# To visualize the shuffled data, we can iterate through it
for element in shuffled_dataset:
    print(element.numpy())
