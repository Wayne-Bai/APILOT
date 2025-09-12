import tensorflow as tf

@tf.function
def my_function(x):
    return x * 2

# Test the function
result = my_function(tf.constant(5))
print(result)
