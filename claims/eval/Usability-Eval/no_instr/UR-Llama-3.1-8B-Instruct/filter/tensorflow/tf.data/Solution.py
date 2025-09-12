# Import required libraries
import tensorflow as tf

# Create a dataset from a list
list_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
dataset = tf.data.Dataset.from_tensor_slices(list_data)

# Map a function to each element in the dataset
def square_element(element):
    return element ** 2

dataset = dataset.map(square_element)

# Batch the dataset
batch_size = 2
dataset = dataset.batch(batch_size)

# Apply transformations to the dataset
# Repeat the dataset for 2 iterations
dataset = dataset.repeat(2)

# Prefetch the dataset
dataset = dataset.prefetch(tf.data.AUTOTUNE)

# Apply a custom transformation to the dataset
def double_element(element):
    return element * 2

dataset = dataset.map(double_element)

# Apply two transformations in parallel
dataset = dataset.apply(tf.data.experimental.group_by_window(
    lambda x: x % 3,
    tf.data.experimental.WindowSizeHint(size=2)
))

def transform_window(window):
    # Transform each element in the window
    return (window.map(lambda x: x * 2), window.map(lambda x: x * 3))

dataset = dataset.apply(tf.data.Dataset.transform_map(transform_window))

# Convert the dataset to a numpy array
numpy_array = dataset.as_numpy_iterator().next()

print(numpy_array)
