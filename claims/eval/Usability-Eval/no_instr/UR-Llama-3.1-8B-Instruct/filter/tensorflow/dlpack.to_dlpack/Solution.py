# Import necessary libraries
import tensorflow as tf
from tensorflow.experimental import dlpack

# Create a sample tensor
tensor = tf.constant([1, 2, 3, 4, 5], shape=[1, 5])

# Convert the tensor to a dlpack capsule representing the tensor
dlpack_capsule = dlpack.from_tensor(tensor)

# Print the dlpack capsule
print(dlpack_capsule)
