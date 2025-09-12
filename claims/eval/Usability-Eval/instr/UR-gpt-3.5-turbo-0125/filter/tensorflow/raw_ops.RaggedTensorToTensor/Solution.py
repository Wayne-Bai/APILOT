
import tensorflow as tf

# Create a ragged tensor
rt = tf.ragged.constant([[1, 2], [3], [4, 5, 6]])

# Convert the ragged tensor to a dense tensor
dense_tensor = tf.RaggedTensor.to_tensor(rt)

print(dense_tensor)
