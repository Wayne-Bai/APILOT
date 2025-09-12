import tensorflow as tf

# Set the value of the dataset iterator's prefetch_to_device attribute to start background threads of asynchronous transformations upon iterator creation
tf.data.experimental.AUTOTUNE

# Set the value of the dataset iterator's prefetch_to_device attribute to start background threads of asynchronous transformations upon iterator creation, as opposed to during the first call to next()
tf.data.experimental.AUTOTUNE

# Set the value of the dataset iterator's prefetch_to_device attribute to start background threads of asynchronous transformations upon iterator creation, as opposed to during the first call to next(), and defaults to False. This improves the latency of the initial 'next()' calls at the expense of requiring more memory to hold prefetched elements between the time of iterator construction and usage.
tf.data.experimental.AUTOTUNE
