
import tensorflow as tf

# Create a tensor with shape (3, 4)
x = tf.random.normal(shape=(3, 4))

# Randomly shuffle the elements of x
shuffled_x = tf.random.shuffle(x)

print(shuffled_x)
