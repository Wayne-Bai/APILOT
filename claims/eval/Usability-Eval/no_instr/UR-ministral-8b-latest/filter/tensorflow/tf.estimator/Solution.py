import tensorflow as tf
from tensorflow.keras import layers, models

class ModelAPI:
    def __init__(self, model, optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy']):
        self.model = model
        self.optimizer = optimizer if optimizer else tf.keras.optimizers.Adam()
        self.loss = loss if loss else 'sparse_categorical_crossentropy'
        self.metrics = metrics if metrics else ['accuracy']

    def compile(self):
        self.model.compile(optimizer=self.optimizer, loss=self.loss, metrics=self.metrics)

    def fit(self, x_train, y_train, x_val, y_val, batch_size=32, epochs=10, validation_freq=1):
        self.model.fit(x_train, y_train, validation_data=(x_val, y_val), batch_size=batch_size, epochs=epochs, verbose=1)

    def evaluate(self, x_test, y_test):
        return self.model.evaluate(x_test, y_test, verbose=1)

    def predict(self, x):
        return self.model.predict(x)

    def save_model(self, file_path):
        self.model.save(file_path)

    def load_model(self, file_path):
        self.model = models.load_model(file_path)

    def summary(self):
        self.model.summary()

# Example of using the ModelAPI
if __name__ == "__main__":
    # Generate a simple model
    input_shape = (28, 28, 1)
    num_classes = 10
    model = models.Sequential([
        layers.Flatten(input_shape=input_shape),
        layers.Dense(128, activation='relu'),
        layers.Dropout(0.2),
        layers.Dense(num_classes, activation='softmax')
    ])

    # Initialize the API with the model
    api = ModelAPI(model)

    # Compile the model
    api.compile()

    # Dummy training/validation data (replace with actual data)
    (x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()
    x_train, x_test = x_train / 255.0, x_test / 255.0
    x_train = x_train[..., tf.newaxis]
    x_test = x_test[..., tf.newaxis]
    x_val = x_train[-1000:].copy()
    y_val = y_train[-1000:].copy()
    x_train = x_train[:-1000].copy()
    y_train = y_train[:-1000].copy()

    # Train the model
    api.fit(x_train, y_train, x_val, y_val)

    # Evaluate the model
    evaluation_results = api.evaluate(x_test, y_test)
    print(f"Evaluation Results: {evaluation_results}")

    # Make predictions
    predictions = api.predict(x_test[:5])
    print(f"Predictions: {predictions}")

    # Save and load the model
    api.save_model("my_model.h5")
    new_model = ModelAPI(models.Sequential())
    new_model.load_model("my_model.h5")

    # Summarize the model
    new_model.summary()
