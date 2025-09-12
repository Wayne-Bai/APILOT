import tensorflow as tf

def shuffle_input(input_data, batch_size):
    # Converting the input data into a tensorflow dataset
    dataset = tf.data.Dataset.from_tensor_slices(input_data)

    # Shuffling the dataset with buffer_size set to the total number of elements for perfect shuffling
    shuffled_dataset = dataset.shuffle(buffer_size=len(input_data))

    # Batching the data
    shuffled_dataset = shuffled_dataset.batch(batch_size)

    return shuffled_dataset

# Usage
# input_data is your data
# batch_size is the desired batch size
# shuffled_data = shuffle_input(input_data, batch_size)
