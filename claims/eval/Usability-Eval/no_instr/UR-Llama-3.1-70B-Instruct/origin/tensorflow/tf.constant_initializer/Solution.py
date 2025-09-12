# Import the necessary library
import tensorflow as tf

# Define a constant initializer
initializer = tf.keras.initializers.Constant(value=0.5)

# Create a variable with the constant initializer
variable = tf.Variable(initializer(shape=[2, 2], dtype=tf.float32))

# Print the variable
print("Tensor with constant values:")
print(variable)

# Output:
# Tensor with constant values:
# tf.Tensor([[0.5 0.5]
#           [0.5 0.5]], shape=(2, 2), dtype=float32)
