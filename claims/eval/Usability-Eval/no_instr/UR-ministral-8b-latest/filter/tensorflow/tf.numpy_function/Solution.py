import tensorflow as tf

@tf.function
def my_function(x):
    y = x + 1
    return y

x = tf.constant([1, 2, 3], dtype=tf.int32)
y = my_function(x)
print(y)
