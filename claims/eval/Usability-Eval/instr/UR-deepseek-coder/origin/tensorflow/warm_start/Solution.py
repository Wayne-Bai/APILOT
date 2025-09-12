import tensorflow as tf

# Define the dataset and transformations
dataset = tf.data.Dataset.from_tensor_slices([1, 2, 3, 4, 5])
dataset = dataset.map(lambda x: x * 2)

# Create an iterator with prefetching enabled
iterator = dataset.prefetch(buffer_size=tf.data.experimental.AUTOTUNE).make_initializable_iterator()

# Initialize the iterator
with tf.Session() as sess:
    sess.run(iterator.initializer)
    
    # Fetch elements from the iterator
    for _ in range(5):
        print(sess.run(iterator.get_next()))
