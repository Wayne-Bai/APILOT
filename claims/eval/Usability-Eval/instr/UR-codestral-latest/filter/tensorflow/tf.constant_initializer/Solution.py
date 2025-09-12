import tensorflow as tf

# Define the constant value
constant_value = 0.5

# Create a constant initializer with the defined value
initializer = tf.keras.initializers.Constant(value=constant_value)

# Apply the initializer to a variable
variable = tf.Variable(initializer([1, 2]))  # Create a 1x2 tensor initialized with the constant value
