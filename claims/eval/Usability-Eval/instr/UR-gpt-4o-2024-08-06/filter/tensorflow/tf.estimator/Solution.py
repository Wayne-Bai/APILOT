import tensorflow as tf

class ModelHandler:
    def __init__(self, model):
        """Initialize with a given Keras model."""
        self.model = model

    def compile_model(self, optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy']):
        """Compile the model with the specified optimizer, loss, and metrics."""
        self.model.compile(optimizer=optimizer, loss=loss, metrics=metrics)

    def train_model(self, train_data, train_labels, epochs=10, batch_size=32, validation_data=None):
        """Train the model using the provided training data and optional validation data."""
        history = self.model.fit(
            train_data,
            train_labels,
            epochs=epochs,
            batch_size=batch_size,
            validation_data=validation_data
        )
        return history

    def evaluate_model(self, test_data, test_labels):
        """Evaluate the model using the provided test data."""
        evaluation = self.model.evaluate(test_data, test_labels)
        return evaluation

    def predict(self, input_data):
        """Predict using the model on the provided input data."""
        predictions = self.model.predict(input_data)
        return predictions

    def export_model(self, model_path):
        """Export the model to the specified path as a TensorFlow SavedModel."""
        self.model.save(model_path, save_format='tf')

# Example usage
if __name__ == "__main__":
    # Define a simple sequential model as an example
    model = tf.keras.Sequential([
        tf.keras.layers.Flatten(input_shape=(28, 28)),
        tf.keras.layers.Dense(128, activation='relu'),
        tf.keras.layers.Dropout(0.2),
        tf.keras.layers.Dense(10, activation='softmax')
    ])

    # Initializing the ModelHandler with the model
    handler = ModelHandler(model)

    # Compile the model
    handler.compile_model()

    # Assume train_images and train_labels are available from a dataset like MNIST
    # handler.train_model(train_images, train_labels, epochs=5)

    # Evaluate the model
    # Assume test_images and test_labels are available
    # evaluation = handler.evaluate_model(test_images, test_labels)

    # Predict
    # predictions = handler.predict(test_images)

    # Export the model to a path
    # handler.export_model('./saved_model')
