import tensorflow as tf

# Create a simple dataset
dataset = tf.data.Dataset.range(10)

# Map a function over the dataset
def map_function(x):
    return x * x

mapped_dataset = dataset.map(map_function)

# Batch the dataset
batched_dataset = mapped_dataset.batch(2)

# Iterate through the dataset and print the results
for batch in batched_dataset:
    print(batch.numpy())
