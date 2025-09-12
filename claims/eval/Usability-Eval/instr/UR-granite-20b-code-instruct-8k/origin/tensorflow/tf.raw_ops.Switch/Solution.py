
import tensorflow as tf
# Define the input tensor
input_tensor = tf.constant([1, 2, 3, 4, 5], dtype=tf.float32)
# Define the predicate tensor
predicate = tf.constant([True, False, True, False, True], dtype=tf.bool)
# Forward data to the output port determined by pred
output_tensor = tf.where(predicate, input_tensor, tf.zeros_like(input_tensor))
