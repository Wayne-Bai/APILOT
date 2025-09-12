import tensorflow as tf

# Create a Dataset from a range of data
dataset = tf.data.Dataset.range(10)

# Apply transformations (e.g., map, batch, shuffle)
# Here, we square the numbers in the data
dataset = dataset.map(lambda x: x * x)

# Shuffle the dataset
dataset = dataset.shuffle(10)

# Batch the dataset (group data into batches of specified size)
dataset = dataset.batch(3)

# Create an iterator to iterate through the dataset
for data in dataset:
    print(data)
