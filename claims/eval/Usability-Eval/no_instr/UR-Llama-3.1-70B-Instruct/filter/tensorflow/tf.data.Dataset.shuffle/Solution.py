# Import necessary libraries
import tensorflow as tf
import numpy as np

# Create some sample data
np.random.seed(0)
data = np.random.rand(10, 5)

# Print original data
print("Original Data:")
print(data)

# Convert data to tensorflow tensor
tensor_data = tf.convert_to_tensor(data)

# Shuffle the data randomly
shuffled_data = tf.random.shuffle(tensor_data)

# Print shuffled data
print("\nShuffled Data:")
print(shuffled_data)

# Create a tensorflow dataset from the data
dataset = tf.data.Dataset.from_tensor_slices(data)

# Shuffle the dataset
shuffled_dataset = dataset.shuffle(buffer_size=1024)

# Print shuffled dataset
print("\nShuffled Dataset:")
for i, batch in enumerate(shuffled_dataset):
    print(batch)
    if i >= 9:
        break

# Alternatively, use tf.random.shuffle for a tensor
tensor = tf.constant(np.arange(20))

# Reshape the tensor into two columns
tensor = tf.reshape(tensor, [10, 2])

# Print original tensor
print("\nOriginal Tensor:")
print(tensor)

# Shuffle the rows of the tensor
shuffled_tensor = tf.random.shuffle(tensor)

# Print shuffled tensor
print("\nShuffled Tensor:")
print(shuffled_tensor)
