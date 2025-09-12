import tensorflow as tf

def elementwise_multiply(x, y):
    result = tf.multiply(x, y)
    return result

# Test the function
x = tf.constant([1, 2, 3, 4, 5], dtype=tf.float32)
y = tf.constant([2, 3, 4, 5, 6], dtype=tf.float32)

output = elementwise_multiply(x, y)
print(output.numpy())
