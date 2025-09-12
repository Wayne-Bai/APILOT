import tensorflow as tf

# Define a simple function to add two numbers
def add_two_numbers(x, y):
 return x + y

# Convert the function into a TensorFlow graph
graph = tf.Graph()
with graph.as_default():
 # Define the input placeholders
 x = tf.placeholder(tf.float32)
 y = tf.placeholder(tf.float32)
 # Call the function with the placeholders as inputs
 result = add_two_numbers(x, y)
 # Define the session to evaluate the graph
 sess = tf.Session(graph=graph)

# Now you can use the graph to evaluate the function
x_val = 2
y_val = 3
result_val = sess.run(result, feed_dict={x: x_val, y: y_val})
print(result_val) # Output: 5
