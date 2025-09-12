import tensorflow as tf

def my_python_function(x):
    return x * x

@tf.function
def my_tensorflow_op(x):
    return my_python_function(x)

# Usage
x = tf.constant(3.0)
result = my_tensorflow_op(x)
print(result)
