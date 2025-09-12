import tensorflow as tf

# Create a TensorFlow variable
variable = tf.Variable([1.0, 2.0, 3.0], name='my_variable')

# Define the shape of the layout
layout = [2, 3]

# Reshape the variable using the defined layout
reshaped_variable = tf.reshape(variable, layout)

# Print the reshaped variable
print(reshaped_variable)
