import tensorflow as tf

# Define a simple dataset
dataset = tf.data.Dataset.from_tensor_slices((tf.constant(1), tf.constant(2)))

# Apply a transformation to the dataset
dataset = dataset.map(lambda x, y: (x * 2, y * 3))

# Perform a batch operation
dataset = dataset.batch(2)

# Perform an infinite loop
for batch in dataset:
    print(batch)
