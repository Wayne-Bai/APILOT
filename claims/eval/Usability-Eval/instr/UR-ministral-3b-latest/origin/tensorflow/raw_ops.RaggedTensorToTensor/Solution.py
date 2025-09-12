import tensorflow as tf

# Create a ragged tensor (an instance of tf.RaggedTensor)
ragged_tensor = tf.ragged.constant([[1, 0, 2], [3, 4], [5, 6, 7, 8]])

# Create a dense tensor using tf.ragged.Dense<T> to possibly alter its shape
dense_tensor = tf.ragged.Dense(ragged_tensor)

print("Original ragged tensor:")
print(ragged_tensor)

print("\nDense tensor:")
print(dense_tensor)
