import tensorflow as tf

# Creating a simple dataset
dataset = tf.data.Dataset.from_tensor_slices([1, 2, 3, 4, 5])

# Applying a transformation to compress the data in practice (e.g., reducing dimensionality, transforming)
# For the sake of illustration, here we perform a simple map transformation that scales each element
def scale_data(x):
    return x * 0.1

# Applying the transformation to the dataset
compressed_dataset = dataset.map(scale_data)

# Iterating through the dataset to see the results
for element in compressed_dataset:
    print(element.numpy())
