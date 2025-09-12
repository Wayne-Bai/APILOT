import tensorflow as tf
from tensorflow import keras

# Define a high-level API function for model training, evaluation, prediction, and exporting
def train_model(model, train_data, train_labels, validation_data, validation_labels, epochs, export_path):
    # Compile the model
    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

    # Train the model
    model.fit(train_data, train_labels, epochs=epochs, validation_data=(validation_data, validation_labels))

    # Evaluate the model
    loss, accuracy = model.evaluate(validation_data, validation_labels)
    print(f'Validation accuracy: {accuracy}')

    # Export the model
    model.save(export_path)
    print(f'Model exported to {export_path}')

# Create a simple model
model = keras.Sequential([
    keras.layers.Dense(64, activation='relu', input_shape=(784,)),
    keras.layers.Dense(10, activation='softmax')
])

# Prepare the data
(train_data, train_labels), (validation_data, validation_labels) = keras.datasets.mnist.load_data()
train_data = train_data / 255.0
validation_data = validation_data / 255.0

# Train the model
train_model(model, train_data, train_labels, validation_data, validation_labels, epochs=5, export_path='model.h5')
