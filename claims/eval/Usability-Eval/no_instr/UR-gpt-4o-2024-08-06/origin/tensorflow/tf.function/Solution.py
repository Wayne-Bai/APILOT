import tensorflow as tf

@tf.function
def simple_add(x, y):
    return x + y

# Now let's create some Tensor and call the function we just compiled
a = tf.constant(5)
b = tf.constant(3)

result = simple_add(a, b)
print(result.numpy())  # Output: 8
