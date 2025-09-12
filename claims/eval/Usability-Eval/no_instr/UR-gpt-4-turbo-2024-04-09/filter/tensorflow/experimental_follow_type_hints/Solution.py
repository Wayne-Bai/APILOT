import tensorflow as tf
import numpy as np

def optimize_computation(arr: np.ndarray) -> tf.Tensor:
    tensor_arr = tf.convert_to_tensor(arr, dtype=tf.float32)
    result = tf.reduce_sum(tensor_arr)
    return result

# Example usage:
arr = np.array([1.0, 2.0, 3.0])
output = optimize_computation(arr)
print(output)
