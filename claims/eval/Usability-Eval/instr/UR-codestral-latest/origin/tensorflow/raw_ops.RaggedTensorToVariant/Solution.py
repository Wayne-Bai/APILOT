import tensorflow as tf

# Assume rt is your RaggedTensor
rt = tf.ragged.constant([[1, 2, 3, 4], [5, 6]])

# Convert RaggedTensor to Dense with default value of 0
dt = rt.to_tensor(default_value=0)
