
import tensorflow as tf

# Create a dataset
dataset = tf.data.Dataset.range(10)

# Create an iterator with prefetching
iterator = dataset.make_initializable_iterator(prefetch_size=None)

# Start background threads of asynchronous transformations upon iterator creation
iterator.initializer.run()
