import tensorflow as tf

# Create a simple dataset using the tf.data API
dataset = tf.data.Dataset.from_tensor_slices([1, 2, 3, 4, 5])

# Apply a transformation to each element in the dataset
dataset = dataset.map(lambda x: x * 2)

# Shuffle the dataset
dataset = dataset.shuffle(buffer_size=5)

# Batch the dataset into groups of 2
dataset = dataset.batch(2)

# Create an iterator to access elements of the dataset
for batch in dataset:
    print(batch.numpy())
