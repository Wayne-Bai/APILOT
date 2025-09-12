import tensorflow as tf

# Assuming you have input data
input_data = tf.random.uniform([1000, 3])  # Replace this with your actual data

# Create a seed for randomness
seed = 42

# Set the seed to ensure reproducibility of output
tf.random.set_seed(seed)

# Shuffle the input data
shuffled_data = tf.reshape(tf.data.Dataset.from_tensor_slices(input_data), (1000, 3))
shuffled_data = shuffled_data.shuffle(buffer_size=1000, seed=seed)

# Print the first few elements of the shuffled data
print(shuffled_data.take(5))
