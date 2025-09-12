
import tensorflow as tf

# Define your model architecture
model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(64, activation='relu', input_shape=(784,)),
    tf.keras.layers.Dense(10, activation='softmax')
])

# Compile the model with a loss function and an optimizer
model.compile(loss='categorical_crossentropy', optimizer='adam')

# Define your input data
inputs = tf.random.normal((128, 784))

# Define your feed and fetch variables
feed_dict = {model.input: inputs}
fetches = [model.output]

# Set up the partial run using TensorFlow's eager execution mode
with tf.device('/GPU:0'):
    model.predict(inputs, steps=1)
