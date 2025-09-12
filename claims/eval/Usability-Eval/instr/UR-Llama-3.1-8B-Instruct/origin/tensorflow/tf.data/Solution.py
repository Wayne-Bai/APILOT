# Import necessary libraries
import tensorflow as tf
import numpy as np

# Create a TensorFlow dataset from a NumPy array
# Here, we're generating some sample data - a list of numbers from 0 to 9
# We'll use this dataset to demonstrate some TensorFlow data operations

# Generate some sample data
data = np.arange(10)

# Convert the NumPy array to a TensorFlow dataset
dataset = tf.data.Dataset.from_tensor_slices(data)

# Print the initial dataset
print("Initial Dataset:")
print(dataset)

# Map a simple function to double each element in the dataset
# We use the `map` method to apply this function to every element in the dataset
doubled_dataset = dataset.map(lambda x: x * 2)

# Print the doubled dataset
print("\nDoubled Dataset:")
print(doubled_dataset)

# Batch the dataset into groups of 3 elements
# We use the `batch` method to create batches of a specified size
batched_dataset = doubled_dataset.batch(3)

# Print the batched dataset
print("\nBatched Dataset:")
print(batched_dataset)

# Convert the dataset to a list
# We use the `as_numpy_iterator` method to convert the dataset to a list
numpy_list = list(batched_dataset.as_numpy_iterator())

# Print the list
print("\nList:")
print(numpy_list)

# Repeat the dataset 3 times
# We use the `repeat` method to repeat the dataset a specified number of times
repeated_dataset = batched_dataset.repeat(3)

# Print the repeated dataset
print("\nRepeated Dataset:")
# Limit the output to the first element
for x in repeated_dataset.take(1):
    print(x)

# Interleave two datasets
# We use the `interleave` method to interleave two datasets
dataset1 = tf.data.Dataset.from_tensor_slices([1, 2, 3])
dataset2 = tf.data.Dataset.from_tensor_slices(['a', 'b', 'c'])

interleaved_dataset = dataset1.interleave(lambda x: dataset2.batch(1))
print("\nInterleaved Dataset:")
print(interleaved_dataset)

# Prefetch the next batch of elements
# We use the `prefetch` method to prefetch the next batch of elements
prefetched_dataset = batched_dataset.prefetch(tf.data.AUTOTUNE)
