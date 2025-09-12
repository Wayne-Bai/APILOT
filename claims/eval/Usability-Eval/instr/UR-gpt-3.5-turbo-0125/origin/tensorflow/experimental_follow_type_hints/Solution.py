
import tensorflow as tf

@tf.function(input_signature=[tf.TensorSpec(shape=[None], dtype=tf.float32)])
def my_function(x):
    return tf.reduce_sum(x)

print(my_function(tf.constant([1.0, 2.0, 3.0])))
