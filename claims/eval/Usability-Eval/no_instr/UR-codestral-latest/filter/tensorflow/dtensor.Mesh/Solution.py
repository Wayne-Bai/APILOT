import tensorflow as tf
import numpy as np

# Define your mesh dimensions
dimensions = [10, 20, 30]

# Create a meshgrid from the dimensions
X = tf.meshgrid(*(tf.range(n, dtype=tf.int32) for n in dimensions))
X = tf.stack(X, axis=-1)

print(X.shape)  # Should output: (10, 20, 30, 3)

# The output tensor X is a 4D tensor where each position (i,j,k) is a 3D coordinate
# matching the index in the original mesh dimensions.
