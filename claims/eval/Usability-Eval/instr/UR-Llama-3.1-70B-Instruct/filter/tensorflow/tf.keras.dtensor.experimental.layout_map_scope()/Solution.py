# Import necessary libraries
import tensorflow as tf

# Define a function to create variables
def create_variables():
    with tf.variable_creator_scope(tf.variable_creator_scope.get_variable):
        variable1 = tf.Variable(10, name="variable1")
        variable2 = tf.Variable(20, name="variable2")
    return variable1, variable2

# Define a custom layout
def custom_layout(memory_address, size, min_location, max_location):
    # Custom allocation strategy
    memory_address += size
    return memory_address

# Create a variable creator scope
with tf.variable_creator_scope(tf.variable_creator_scope.get_variable, 
                                allocation_strategy=lambda size: custom_layout(0, size, 0, 100)):
    variable1, variable2 = create_variables()

# Print the variables
print(variable1)
print(variable2)
