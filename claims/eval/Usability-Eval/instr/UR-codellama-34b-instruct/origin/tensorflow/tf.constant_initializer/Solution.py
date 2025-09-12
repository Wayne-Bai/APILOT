import tensorflow as tf

# Create a constant initializer with a value of 10
constant_initializer = tf.keras.initializers.Constant(value=10)

# Use the initializer to create a tensor
tensor = constant_initializer((3, 4))

print(tensor)
