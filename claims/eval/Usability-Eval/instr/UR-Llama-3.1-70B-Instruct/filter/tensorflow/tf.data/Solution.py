# Importing necessary libraries
import tensorflow as tf
from tensorflow.data import *

# Creating a dataset from a list of elements
def create_dataset(elements):
    return tf.data.Dataset.from_tensor_slices(elements)

# Creating a dataset from a generator
def create_dataset_from_generator(generator_fn, output_types, output_shapes=None):
    return tf.data.Dataset.from_generator(generator_fn, output_types, output_shapes)

# Creating a range dataset
def create_range_dataset(start, stop, step=1):
    return tf.data.Dataset.range(start, stop, step)

# Reading lines from a text file
def read_text_lines(filename):
    return tf.data.TextLineDataset([filename])

# Creating a batched dataset from a dataset
def create_batched_dataset(dataset, batch_size):
    return dataset.batch(batch_size)

# Prefetching a dataset
def prefetch_dataset(dataset, buffer_size):
    return dataset.prefetch(buffer_size)

# Creating a map function for dataset
def create_map_fn(dataset, map_fn):
    return dataset.map(map_fn)

# Creating a reduce function for dataset
def create_reduce_fn(dataset, initial_state, reduce_fn):
    return dataset.reduce(initial_state, reduce_fn)

# Creating a filter function for dataset
def create_filter_fn(dataset, filter_fn):
    return dataset.filter(filter_fn)

# Creating an iterator for a dataset
def create_iterator(dataset):
    return iter(dataset)

# Example usage
if __name__ == "__main__":
    # Creating a dataset from a list of elements
    dataset = create_dataset([1, 2, 3, 4, 5])

    # Creating a batched dataset
    batched_dataset = create_batched_dataset(dataset, 2)
    print("Batched dataset:", list(batched_dataset))

    # Creating a map function for dataset
    def map_fn(x):
        return x * 2

    mapped_dataset = create_map_fn(dataset, map_fn)
    print("Mapped dataset:", list(mapped_dataset))

    # Creating a reduce function for dataset
    def reduce_fn(state, x):
        return state + x

    reduced_dataset = create_reduce_fn(dataset, 0, reduce_fn)
    print("Reduced dataset:", reduced_dataset)

    # Creating a filter function for dataset
    def filter_fn(x):
        return x % 2 == 0

    filtered_dataset = create_filter_fn(dataset, filter_fn)
    print("Filtered dataset:", list(filtered_dataset))
