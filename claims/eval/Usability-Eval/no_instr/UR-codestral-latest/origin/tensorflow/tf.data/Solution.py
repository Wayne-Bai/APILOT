import tensorflow as tf

# Create a list of numbers
numbers = [1, 2, 3, 4, 5]

# Create a data set from the list
dataset = tf.data.Dataset.from_tensor_slices(numbers)

# Print the elements of the dataset
for elem in dataset:
    print(elem)
