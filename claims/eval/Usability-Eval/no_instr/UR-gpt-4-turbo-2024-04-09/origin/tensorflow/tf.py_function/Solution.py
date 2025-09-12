import tensorflow as tf

def my_python_function(x):
    return x * 2

@tf.function
def tensorflow_function(input_tensor):
    eager_result = tf.py_function(func=my_python_function, inp=[input_tensor], Tout=tf.float32)
    return eager_result

# Example usage
input_tensor = tf.constant([1.0, 2.0, 3.0, 4.0])
result_tensor = tensorflow_function(input_tensor)
print(result_tensor)
