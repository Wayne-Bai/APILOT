
import tensorflow as tf

# Create a dataset from some input data
input_data = ...
dataset = tf.data.Dataset.from_tensor_slices(input_data)

# Shuffle the dataset
shuffled_dataset = dataset.shuffle(100, reshuffle_each_iteration=True)

# Print out the shuffled data
for batch in shuffled_dataset:
  print(batch)
