import tensorflow as tf

# Define the function to be compiled
@tf.function
def my_function(x, y):
    return tf.add(x, y)

# Compile the function into a callable TensorFlow graph
compiled_function = my_function.get_concrete_function(
    tf.TensorSpec(shape=(None, 1), dtype=tf.float32),
    tf.TensorSpec(shape=(None, 1), dtype=tf.float32)
)