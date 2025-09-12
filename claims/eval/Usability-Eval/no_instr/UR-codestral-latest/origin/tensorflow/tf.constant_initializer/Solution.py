import tensorflow as tf

# Create an initializer that generates tensors with constant values.
const_init = tf.constant_initializer(value=0.1)

# Use the initializer to initialize a tensor with a shape of (3, 3)
tensor = tf.Variable(const_init(shape=(3, 3)))

# Ensure the tensor is initialized
init = tf.global_variables_initializer()

# Run the initialization
with tf.Session() as sess:
    sess.run(init)
    print(sess.run(tensor))
