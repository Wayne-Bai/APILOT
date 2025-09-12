import tensorflow as tf

def shuffle_data(input_data):
    shuffled_data = tf.random.shuffle(input_data)
    return shuffled_data

# Example usage:
# input_data = tf.constant([1, 2, 3, 4, 5])
# shuffled_data = shuffle_data(input_data)
# print(shuffled_data.numpy())
