# Import necessary libraries
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import numpy as np

# Define a custom initializer class
class CustomInitializer(tf.keras.initializers.Initializer):
    def __init__(self, mean=0.0, stddev=1.0):
        self.mean = mean
        self.stddev = stddev

    def __call__(self, shape, dtype=None, **kwargs):
        return tf.random.normal(shape, mean=self.mean, stddev=self.stddev, dtype=dtype)

    def get_config(self):
        return {'mean': self.mean,'stddev': self.stddev}

# Define a custom layer class to test the initializer
class CustomLayer(layers.Layer):
    def __init__(self, units, initializer):
        super(CustomLayer, self).__init__()
        self.units = units
        self.initializer = initializer

    def build(self, input_shape):
        self.kernel = self.add_weight("kernel",
                                      shape=[int(input_shape[-1]),
                                             self.units],
                                      initializer=self.initializer)

    def call(self, inputs):
        return tf.matmul(inputs, self.kernel)

# Create a model using the custom layer and initializer
model = keras.Sequential([
    CustomLayer(10, CustomInitializer(mean=1.0, stddev=0.01)),
    layers.Activation("relu"),
    layers.Dense(5)
])

# Compile the model
model.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"])

# Test the model
x = np.random.rand(100, 784)
y = np.random.randint(0, 5, 100)

model.fit(x, y, epochs=1)

# Serialize the model
config = model.get_config()

# Deserialize the model
new_model = keras.Model.from_config(config)

print(new_model.get_config())
