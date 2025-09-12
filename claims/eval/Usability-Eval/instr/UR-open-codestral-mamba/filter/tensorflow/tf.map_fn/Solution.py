import tensorflow as tf

def my_func(x):
    # This function takes a tensor x and performs a specific operation on each element.
    # Replace the operation below with the desired operation for your use case.
    return x * 2

# Create a TensorFlow dataset from a list
input_data = [1, 2, 3, 4, 5]
dataset = tf.data.Dataset.from_tensor_slices(input_data)

# Transforms elems by applying fn to each element unstacked on axis 0
transformed_dataset = dataset.map(my_func)

# Convert the transformed dataset to a list for printing results
transformed_data = list(transformed_dataset)

transformed_data
