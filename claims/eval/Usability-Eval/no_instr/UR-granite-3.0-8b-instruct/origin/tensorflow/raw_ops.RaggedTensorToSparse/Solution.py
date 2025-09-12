import tensorflow as tf

# Assuming 'ragged' is your RaggedTensor
# Convert RaggedTensor to SparseTensor
sparse_tensor = tf.RaggedToSparseTensor(ragged)
