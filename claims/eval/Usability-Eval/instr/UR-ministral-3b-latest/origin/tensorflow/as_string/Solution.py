import tensorflow as tf

# Assume we have a tensor named 'tensor'
tensor = tf.constant([123, 456, 789])

# Convert each entry in the tensor to strings
str_tensor = tf.map_fn(lambda x: tf.cast(x, tf.string), tensor)

print(str_tensor)
