import tensorflow as tf

# Assuming 'params' is a Tensor and 'indices' is a Tensor of the same type (usually int64)
params = tf.constant([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
indices = tf.constant([0, 1, 2, 0, 1])

gathered_params = tf.gather(params, indices)

print(gathered_params)
