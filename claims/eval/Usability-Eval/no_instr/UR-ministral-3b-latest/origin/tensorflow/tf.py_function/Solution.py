import tensorflow as tf

def add(a, b):
    return a + b

add_tf_op = tf.function(add)

# Example of how to use add_tf_op
x = tf.constant(5)
y = tf.constant(3)
result = add_tf_op(x, y)
print(result)
