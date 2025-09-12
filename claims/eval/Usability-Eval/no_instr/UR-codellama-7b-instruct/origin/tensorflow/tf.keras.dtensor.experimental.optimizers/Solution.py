
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.experimental.dtensor import experimental_optimizers

def train_model(model, x, y):
    # Compile the model with an optimizer
    opt = experimental_optimizers.OnePlus(learning_rate=0.01)
    model.compile(optimizer=opt, loss='sparse_categorical_crossentropy', metrics=['accuracy'])

    # Train the model on the data
    model.fit(x, y, epochs=5)
