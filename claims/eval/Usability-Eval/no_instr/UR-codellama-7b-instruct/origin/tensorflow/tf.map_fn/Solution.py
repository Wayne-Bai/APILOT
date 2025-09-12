import tensorflow as tf

# Define the function to apply to each element in the tensor
def my_func(x):
    return x ** 2

# Create a tensor with shape (3, 4)
t = tf.constant([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

# Transform the elements of the tensor using my_func()
result = tf.map_fn(my_func, t)

print(result) # Output: <tf.Tensor 'tf.function_3/while/tensor_transpose_5:0' shape=(3, 4) dtype=float32>
