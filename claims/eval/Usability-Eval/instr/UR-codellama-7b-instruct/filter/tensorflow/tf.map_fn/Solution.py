import tensorflow as tf

# Define a function to apply to each element in the tensor
def my_function(x):
  return x ** 2

# Create a tensor with shape (3, 4) and fill it with random data
tensor = tf.random.normal([3, 4], mean=0.0, stddev=1.0, dtype=tf.float64)

# Apply the function to each element in the tensor using map_fn
result = tf.map_fn(my_function, tensor, dtype=tf.float64)

print(result)
