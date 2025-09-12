import tensorflow as tf

# Define the input dataset
input_dataset = tf.data.Dataset.from_tensor_slices([1, 2, 3, 4, 5])

# Compress the dataset element
compressed_dataset = input_dataset.map(tf.io.serialize_tensor)

# Print the compressed dataset
for element in compressed_dataset:
    print(element.numpy())
