import tensorflow as tf

# Create a RaggedTensor
rt = tf.ragged.constant([
    [0, 1, 2, 3],
    [4, 5],
    [6],
    []
])

# Load RaggedTensor into a Variant Tensor
variable_tensor = tf.Variable(rt)

# Print to check
print(variable_tensor)
