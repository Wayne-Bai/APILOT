import tensorflow as tf

# Input data
data = ['a', 'b', 'c']

# Randomly shuffle input data
shuffled_data = tf.random.shuffle(data)

print(shuffled_data)  # Output: ['b', 'a', 'c']
