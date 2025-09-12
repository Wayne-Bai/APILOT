import tensorflow as tf

# Define the layout for the Variables
layout = tf.VariableLayout(compressed_dim=10, offset=2)

# Create a scope to contain the Variables
with tf.VariableScope('MyScope', use_resource=True, layout=layout):
    # Create some Variables within the scope
    var1 = tf.get_variable('var1', shape=[10, 10])
    var2 = tf.get_variable('var2', shape=[10, 10])
