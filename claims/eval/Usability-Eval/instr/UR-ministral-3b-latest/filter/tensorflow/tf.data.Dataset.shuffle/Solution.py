import tensorflow as tf

# Assume `data` is your input data
data = tf.data.Dataset.from_tensor_slices([...])  # Your input data here

# Create a buffer of data and shuffle it
buffered_data = data.shuffle(buffer_size=1024, reshuffle_each_iteration=True)

# Start a new iterator to iterate over the shuffled data
iterator = buffered_data.fetch_next()

# Iterate over the data
for value in iterator:
    print(value)
