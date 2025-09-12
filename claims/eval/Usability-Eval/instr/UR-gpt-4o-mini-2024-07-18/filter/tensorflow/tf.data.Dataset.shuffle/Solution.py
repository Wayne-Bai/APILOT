import tensorflow as tf

def random_shuffle(data, seed=None):
    # Shuffle the input data
    shuffled_data = tf.random.shuffle(data, seed=seed)
    return shuffled_data

# Example usage
data = tf.constant([[1, 2], [3, 4], [5, 6]])
shuffled_data = random_shuffle(data)
print(shuffled_data)
