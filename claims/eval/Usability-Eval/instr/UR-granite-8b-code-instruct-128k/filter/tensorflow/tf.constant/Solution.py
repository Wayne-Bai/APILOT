import tensorflow as tf

# Example 1: Create a constant tensor from a list
list_of_floats = [1.0, 2.0, 3.0]
const_list = tf.constant(list_of_floats)
print(const_list)

# Output: tf.Tensor([1. 2. 3.], shape=(3,), dtype=float32)

# Example 2: Create a constant tensor from a numpy array
import numpy as np
np_array = np.array([4.0, 5.0, 6.0])
const_np_array = tf.constant(np_array)
print(const_np_array)

# Output: tf.Tensor([4. 5. 6.], shape=(3,), dtype=float32)

# Example 3: Create a constant tensor from a 2-D numpy array
np_2d_array = np.array([[7.0, 8.0], [9.0, 10.0]])
const_np_2d_array = tf.constant(np_2d_array)
print(const_np_2d_array)

# Output: tf.Tensor(
# [[7. 8.]
# [9. 10.]], shape=(2, 2), dtype=float32)