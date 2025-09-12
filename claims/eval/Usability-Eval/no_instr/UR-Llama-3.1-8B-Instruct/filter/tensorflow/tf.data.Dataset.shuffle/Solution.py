# Import necessary libraries
import tensorflow as tf
import numpy as np

# Create a sample dataset
# For demonstration purposes, let's create a 2D dataset with 10 rows and 3 columns
dataset = tf.data.Dataset.from_tensor_slices(
    np.random.randint(0, 100, size=(10, 3))
)

# Print the original dataset
print("Original Dataset:")
print(dataset)

# Randomly shuffling the input data
dataset_shuffled = dataset.shuffle(buffer_size=len(dataset))

# Print the shuffled dataset
print("Shuffled Dataset:")
for item in dataset_shuffled.take(5):
    print(item)

