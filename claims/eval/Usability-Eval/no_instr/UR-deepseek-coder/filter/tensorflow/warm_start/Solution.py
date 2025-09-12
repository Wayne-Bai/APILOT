import tensorflow as tf

# Define a dataset with some transformations
dataset = tf.data.Dataset.from_tensor_slices([1, 2, 3, 4, 5])
dataset = dataset.map(lambda x: x * 2)  # Example transformation

# Create an iterator with `experimental_prefetch_to_device` set to True
# This will start background threads for asynchronous transformations upon iterator creation
iterator = dataset.prefetch(tf.data.experimental.AUTOTUNE).make_initializable_iterator()

# Initialize the iterator
with tf.Session() as sess:
    sess.run(iterator.initializer)
    
    # Now you can call next() without the initial latency
    for _ in range(5):
        print(sess.run(iterator.get_next()))
