import tensorflow as tf

@tf.function
def my_function(x, y):
    return x + y

# Example usage
x = tf.constant(5)
y = tf.constant(3)
result = my_function(x, y)

print(result.numpy())  # Output: 8
