import tensorflow as tf

# Example of using the experimental optimizers from the tf.keras.dtensor namespace
class SimpleModel(tf.keras.Model):
    def __init__(self):
        super(SimpleModel, self).__init__()
        self.dense_layer = tf.keras.layers.Dense(10, activation='relu')

    def call(self, inputs):
        return self.dense_layer(inputs)

# Create an instance of the model
model = SimpleModel()

# Define an experimental optimizer
optimizer = tf.keras.dtensor.experimental.optimizers.SGD(learning_rate=0.01)

# Compile the model with the optimizer and a loss function
model.compile(optimizer=optimizer, loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Dummy data for demonstration
import numpy as np
x_train = np.random.rand(100, 20).astype(np.float32)
y_train = np.random.randint(0, 10, size=(100,))

# Fit the model
model.fit(x_train, y_train, epochs=5)
