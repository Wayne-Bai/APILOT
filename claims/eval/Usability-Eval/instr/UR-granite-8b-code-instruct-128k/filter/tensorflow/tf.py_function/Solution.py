
import tensorflow as tf

@tf.function
def my_python_function(x):
  return x * x

my_tf_function = tf.function(lambda x: my_python_function(x))

print(my_tf_function(2))  # Prints 4
