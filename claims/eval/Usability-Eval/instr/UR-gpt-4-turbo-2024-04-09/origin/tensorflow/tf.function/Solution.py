import tensorflow as tf

@tf.function
def compiled_function(x, y):
    return x * y + tf.constant(10)

# Example usage
x = tf.constant(5)
y = tf.constant(3)
result = compiled_function(x, y)
print("Result: ", result.numpy())
