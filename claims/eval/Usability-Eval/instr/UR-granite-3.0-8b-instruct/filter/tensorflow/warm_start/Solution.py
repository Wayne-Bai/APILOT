import tensorflow as tf

# Define a dataset
dataset = tf.data.Dataset.from_tensor_slices([1, 2, 3, 4, 5])

# Define a transformation function
def transform_function(x):
    return x * 2

# Apply the transformation function to the dataset
dataset = dataset.map(transform_function)

# Create a prefetch transformation to improve the latency of the initial 'next()' calls
dataset = dataset.prefetch(buffer_size=tf.data.experimental.AUTOTUNE)

# Start background threads of asynchronous transformations upon iterator creation
dataset = dataset.prefetch(buffer_size=tf.data.experimental.AUTOTUNE, use_interleave=True)

# Iterate over the dataset
for item in dataset:
    print(item.numpy())
