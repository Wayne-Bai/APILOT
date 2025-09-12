import tensorflow as tf

@tf.function
def my_function(x):
    return tf.add(x, 1)

my_function(tf.constant([1, 2, 3]))

print(my_function.experimental_get_static_function())
