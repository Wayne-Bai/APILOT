import tensorflow as tf
from tensorflow.keras import layers, models

class ModelHandler:
    def __init__(self, model, optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy']):
        self.model = model
        self.optimizer = optimizer
        self.loss = loss
        self.metrics = metrics

    def compile_model(self):
        self.model.compile(optimizer=self.optimizer, loss=self.loss, metrics=self.metrics)

    def train(self, train_data, train_labels, epochs=10, validation_data=None):
        self.model.fit(train_data, train_labels, epochs=epochs, validation_data=validation_data)

    def evaluate(self, test_data, test_labels):
        return self.model.evaluate(test_data, test_labels)

    def predict(self, data):
        return self.model.predict(data)

    def save_model(self, path):
        self.model.save(path)

    @staticmethod
    def load_model(path):
        return tf.keras.models.load_model(path)

# Example usage:
if __name__ == "__main__":
    # Define a simple model
    model = models.Sequential([
        layers.Dense(64, activation='relu', input_shape=(784,)),
        layers.Dense(10, activation='softmax')
    ])

    # Create an instance of ModelHandler
    model_handler = ModelHandler(model)

    # Compile the model
    model_handler.compile_model()

    # Example data (replace with actual data)
    train_data = tf.random.normal([1000, 784])
    train_labels = tf.random.uniform([1000], maxval=10, dtype=tf.int32)
    test_data = tf.random.normal([200, 784])
    test_labels = tf.random.uniform([200], maxval=10, dtype=tf.int32)

    # Train the model
    model_handler.train(train_data, train_labels, epochs=5)

    # Evaluate the model
    loss, accuracy = model_handler.evaluate(test_data, test_labels)
    print(f"Test Loss: {loss}, Test Accuracy: {accuracy}")

    # Predict with the model
    predictions = model_handler.predict(test_data[:5])
    print("Predictions:", predictions)

    # Save the model
    model_handler.save_model('my_model.h5')

    # Load the model
    loaded_model = ModelHandler.load_model('my_model.h5')
    print("Model loaded successfully.")
