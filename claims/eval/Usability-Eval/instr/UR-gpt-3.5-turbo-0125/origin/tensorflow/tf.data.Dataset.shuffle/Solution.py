
import tensorflow as tf

# Create a dataset from input data
input_data = tf.constant([[1, 2], [3, 4], [5, 6], [7, 8]])
dataset = tf.data.Dataset.from_tensor_slices(input_data)

# Shuffle the dataset
shuffled_dataset = dataset.shuffle(buffer_size=4)

# Iterate over the shuffled dataset
for data in shuffled_dataset:
    print(data)
