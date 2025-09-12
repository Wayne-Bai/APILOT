
import tensorflow as tf

# Define a function with a custom gradient
def custom_gradient(x):
    return x**2, (2*x,)

# Use the function in a TensorFlow model
model = tf.keras.models.Sequential([
    tf.keras.layers.InputLayer((1,)),
    tf.keras.layers.Dense(64, activation=tf.nn.relu),
    tf.keras.layers.Dense(64, activation=tf.nn.relu),
    tf.keras.layers.Dense(10, activation=tf.nn.softmax)
])

# Compile the model with a custom optimizer and loss function
model.compile(optimizer='adam', loss=custom_gradient)
