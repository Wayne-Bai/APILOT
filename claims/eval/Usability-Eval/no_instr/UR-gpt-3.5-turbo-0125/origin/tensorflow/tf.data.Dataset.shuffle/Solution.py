
import tensorflow as tf

# Generate input data
input_data = tf.constant([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Randomly shuffle input data
shuffled_data = tf.random.shuffle(input_data)

print("Shuffled Data:")
print(shuffled_data)
