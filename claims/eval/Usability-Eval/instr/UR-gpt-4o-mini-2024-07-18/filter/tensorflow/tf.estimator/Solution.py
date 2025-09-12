import tensorflow as tf

class ModelManager:
    def __init__(self, model, optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy']):
        self.model = model
        self.model.compile(optimizer=optimizer, loss=loss, metrics=metrics)

    def train(self, train_dataset, validation_dataset, epochs):
        history = self.model.fit(train_dataset, validation_data=validation_dataset, epochs=epochs)
        return history

    def evaluate(self, test_dataset):
        evaluation = self.model.evaluate(test_dataset)
        return evaluation

    def predict(self, input_data):
        predictions = self.model.predict(input_data)
        return predictions

    def save_model(self, filepath):
        self.model.save(filepath)

    def load_model(self, filepath):
        self.model = tf.keras.models.load_model(filepath)

# Example of usage:
# model = tf.keras.Sequential([...])  # Define your tf model architecture here
# manager = ModelManager(model)
# history = manager.train(train_dataset, validation_dataset, epochs=10)
# evaluation = manager.evaluate(test_dataset)
# predictions = manager.predict(input_data)
# manager.save_model('path_to_save_model')
