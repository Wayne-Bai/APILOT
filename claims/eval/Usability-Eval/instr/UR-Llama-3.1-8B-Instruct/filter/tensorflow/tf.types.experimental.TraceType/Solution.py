# Import necessary tensorflow modules
import tensorflow as tf

# Define a simple function to test the tf.function
@tf.function
def add(x, y):
    return x + y

# Test the function
result = add(3, 5)
print(result)

# Print the function source code
print(add.experimental_unwrapt())

# Print the function estimated-type spec (representing the type of the objects returned by the function)
print(add.structured_value_signature())

# Create a graph-type spec (representing the type of the objects returned by the function) manually
x = tf.constant(3)
y = tf.constant(5)
graph_type_spec = tf.TensorSpec([tf.TensorShape(None)])

# Apply the graph-type spec to the result of the add function
result_with_type_spec = tf.strings.as_string(add(x, y), graph_type_spec)
print(result_with_type_spec)
