import tensorflow as tf

# Create a simple dataset
dataset = tf.data.Dataset.range(10)

# Apply asynchronous transformations to the dataset
def async_transform(x):
    return x * 2

dataset = dataset.map(async_transform, num_parallel_calls=tf.data.AUTOTUNE)

# Create an iterator with the 'experimental_prefetch_to_device' method
# and set the 'experimental_autocancel' option to False to enable 
# background threads of asynchronous transformations upon iterator creation
options = tf.data.Options()
options.experimental_prefetch_to_device('/device:CPU:0')
options.experimental_autocancel = False
options.experimental_threading.max_intra_op_parallelism = 1
dataset = dataset.with_options(options)

# Iterate through the dataset
iterator = iter(dataset)

# Print the results
for _ in range(10):
    print(next(iterator))
