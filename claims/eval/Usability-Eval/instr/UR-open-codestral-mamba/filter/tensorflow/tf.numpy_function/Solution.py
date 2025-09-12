import tensorflow as tf

def my_function(x):
    return x**2

# Wrap the function as a TensorFlow operation
my_tf_function = tf.function(my_function)

# Now, you can use it just like any other TensorFlow operation
x = tf.constant(4)
result = my_tf_function(x)
print(result)  # Output: <tf.Tensor: shape=(), dtype=int32, numpy=16>
