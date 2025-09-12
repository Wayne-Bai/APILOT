import tensorflow as tf

# Define the layout function
def apply_layout(var):
    # Example layout: Add a prefix to the variable name
    var._handle_name = f"custom_prefix/{var.name}"

# Create a custom variable scope with the layout function
with tf.variable_scope("my_scope", custom_getter=apply_layout):
    # Create some variables under this scope
    var1 = tf.Variable(initial_value=1.0, name="var1")
    var2 = tf.Variable(initial_value=2.0, name="var2")

# Print the variables to see the applied layout
print(var1.name)  # Output: custom_prefix/my_scope/var1:0
print(var2.name)  # Output: custom_prefix/my_scope/var2:0
