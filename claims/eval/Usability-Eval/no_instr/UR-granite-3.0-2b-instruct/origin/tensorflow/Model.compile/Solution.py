import tensorflow as tf
from tensorflow.keras import layers

# Define the model architecture
class MyModel(tf.keras.Model):
    def __init__(self):
        super(MyModel, self).__init__()
        self.dense1 = layers.Dense(64, activation='relu')
        self.dense2 = layers.Dense(10, activation='softmax')

    def call(self, x):
        x = self.dense1(x)
        return self.dense2(x)

# Create an instance of the model
model = MyModel()

# Print the model summary
model.summary()
