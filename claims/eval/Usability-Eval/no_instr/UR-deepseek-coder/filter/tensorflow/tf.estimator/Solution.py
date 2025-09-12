import tensorflow as tf
from tensorflow.keras import layers, models

class ModelWrapper:
    def __init__(self, input_shape, num_classes):
        self.model = models.Sequential([
            layers.Input(shape=input_shape),
            layers.Conv2D(32, (3, 3), activation='relu'),
            layers.MaxPooling2D((2, 2)),
            layers.Conv2D(64, (3, 3), activation='relu'),
            layers.MaxPooling2D((2, 2)),
            layers.Conv2D(64, (3, 3), activation='relu'),
            layers.Flatten(),
            layers.Dense(64, activation='relu'),
            layers.Dense(num_classes, activation='softmax')
        ])
        self.model.compile(optimizer='adam',
                           loss='sparse_categorical_crossentropy',
                           metrics=['accuracy'])

    def train(self, train_data, train_labels, epochs=10, validation_data=None):
        self.model.fit(train_data, train_labels, epochs=epochs, validation_data=validation_data)

    def evaluate(self, test_data, test_labels):
        return self.model.evaluate(test_data, test_labels)

    def predict(self, data):
        return self.model.predict(data)

    def export_model(self, export_path):
        self.model.save(export_path)

# Example usage:
# model_wrapper = ModelWrapper(input_shape=(28, 28, 1), num_classes=10)
# model_wrapper.train(train_data, train_labels, epochs=10, validation_data=(val_data, val_labels))
# model_wrapper.evaluate(test_data, test_labels)
# predictions = model_wrapper.predict(some_data)
# model_wrapper.export_model('path_to_save_model')
