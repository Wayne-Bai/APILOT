import tensorflow as tf

# Create a dataset with asynchronous transformations
dataset = tf.data.Dataset.from_tensor_slices((tf.constant(1), tf.constant(2), tf.constant(3))) \
    .map(lambda x, y, z: (tf.Variable(x), tf.Variable(y), tf.Variable(z))) \
    .batch(3) \
    .prefetch(tf.data.experimental.AUTOTUNE)

# Print the dataset
for element in dataset:
    print(element)
