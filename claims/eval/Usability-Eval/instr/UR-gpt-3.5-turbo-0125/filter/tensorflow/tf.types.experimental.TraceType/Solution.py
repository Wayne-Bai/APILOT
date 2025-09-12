
import tensorflow as tf

@tf.function(input_signature=[tf.TensorSpec(shape=[None], dtype=tf.float32)])
def process_data(input_data):
    return tf.reduce_sum(input_data)

input_data = tf.constant([1.0, 2.0, 3.0, 4.0])
result = process_data(input_data)
print(result)
