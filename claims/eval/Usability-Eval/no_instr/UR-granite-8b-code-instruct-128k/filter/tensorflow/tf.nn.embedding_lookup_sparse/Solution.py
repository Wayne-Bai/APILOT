import tensorflow as tf

# Assuming 'ids' and 'weights' are TensorFlow tensors and 'tensors' is a list of TensorFlow tensors
embedded_sum = tf.reduce_sum(tf.stack([tf.gather(t, ids) * weights for t in tensors]), axis=0)
