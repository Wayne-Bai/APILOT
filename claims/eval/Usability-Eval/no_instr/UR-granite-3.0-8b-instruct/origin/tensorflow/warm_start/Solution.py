import tensorflow as tf

# Create a dataset
dataset = tf.data.Dataset.from_tensor_slices([1, 2, 3, 4, 5])

# Set prefetch_input_elements to True to start background threads
dataset = dataset.prefetch(buffer_size=tf.data.experimental.AUTOTUNE)

# Iterate over the dataset
for element in dataset:
    print(element.numpy())
