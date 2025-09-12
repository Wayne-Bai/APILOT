import tensorflow as tf

# Create a simple TensorFlow graph
sess = tf.Session()

# Define a constant tensor
constant_tensor = tf.constant(5.0)

# Define a variable tensor
variable_tensor = tf.Variable(3.0)

# Define an operation to add the constant and variable tensors
add_operation = tf.add(constant_tensor, variable_tensor)

# Initialize the variables
init = tf.global_variables_initializer()
sess.run(init)

# Start the execution
for i in range(10):
    # Fetch the result of the addition operation
    result = sess.run(add_operation)
    print(f"Iteration {i+1}: {result}")
