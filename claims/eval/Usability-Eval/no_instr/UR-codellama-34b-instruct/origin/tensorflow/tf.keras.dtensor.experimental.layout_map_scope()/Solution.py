import tensorflow as tf

# Define a function that will be used to create a variable with the desired layout
def create_variable(shape, dtype, initializer, regularizer):
    return tf.get_variable("var", shape=shape, dtype=dtype, initializer=initializer, regularizer=regularizer)

# Create a scope and apply the layout to all variables created under it
with tf.compat.v1.variable_scope("my_scope", custom_layout=tf.layout.fixed(64)):
    # Create some variables using the function we defined above
    x = create_variable([2, 3], tf.float32, initializer=tf.zeros_initializer(), regularizer=tf.contrib.layers.l2_regularizer())
    y = create_variable([4, 5], tf.float32, initializer=tf.ones_initializer(), regularizer=tf.contrib.layers.l1_regularizer())

# Print the layout of the variables
print(x.layout)  # Output: Fixed64
print(y.layout)  # Output: Fixed64
