import tensorflow as tf

def my_function():
    return tf.constant([1, 2, 3, 4, 5])

# Wrapping the function as a TensorFlow op using tf.py_function
@tf.function
def tensorflow_my_function():
    return tf.py_function(my_function, [], tf.int32)

# Example usage:
result = tensorflow_my_function()
print(result.numpy())
