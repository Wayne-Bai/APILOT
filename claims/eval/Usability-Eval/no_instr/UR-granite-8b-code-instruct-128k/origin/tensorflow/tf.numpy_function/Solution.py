import tensorflow as tf

def my_python_function(x):
    return x + 1

@tf.function
def my_tensorflow_op(x):
    return my_python_function(x)

x = tf.constant(5)
result = my_tensorflow_op(x)
print(result)
