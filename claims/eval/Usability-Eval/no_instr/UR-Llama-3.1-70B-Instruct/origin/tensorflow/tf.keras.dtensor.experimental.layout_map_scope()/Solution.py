# Importing the necessary library
import tensorflow as tf

# Define a function with a specific layout
def create_variables(scope_name):
    with tf.compat.v1.variable_scope(scope_name) as scope:
        # Apply a specific layout to all the tf.Variables created under the scope
        layout = tf.compat.v1.variable_op_scope([scope], lambda layout: layout)
        with layout:
            var1 = tf.Variable([1.0, 2.0])
            var2 = tf.Variable([3.0, 4.0])
            return var1, var2

# Create the variables with the specified scope and layout
var1, var2 = create_variables('my_scope')

# Print the variables
print(var1)
print(var2)

# To initialize all the variables in a TensorFlow Session
init_op = tf.compat.v1.global_variables_initializer()

# Run the Session
sess = tf.compat.v1.Session()
sess.run(init_op)

print(sess.run(var1))
print(sess.run(var2))

# Close the Session when we are done
sess.close()
