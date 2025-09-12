import tensorflow as tf

# Define a function that takes a single argument and returns a dataset object
def data_to_dataset(x):
    # Convert the input to a dataset object
    dataset = tf.data.Dataset.from_tensor_slices(x)
    return dataset

# Call the function with an example input
example_input = np.array([1, 2, 3])
example_output = data_to_dataset(example_input)

# Print the output to demonstrate that it is a valid Dataset object
print(type(example_output))
