import tensorflow as tf
from tensorflow import keras
from sklearn.base import ClassifierMixin

class CustomClassifier(ClassifierMixin):
    def __init__(self, input_shape, num_classes, hidden_units=32, epochs=10):
        self.input_shape = input_shape
        self.num_classes = num_classes
        self.hidden_units = hidden_units
        self.epochs = epochs
        self.model = self._build_model()

    def _build_model(self):
        model = keras.Sequential([
            keras.layers.Input(shape=self.input_shape),
            keras.layers.Dense(self.hidden_units, activation='relu'),
            keras.layers.Dense(self.num_classes, activation='softmax')
        ])
        model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
        return model

    def fit(self, X, y):
        self.model.fit(X, y, epochs=self.epochs)

    def predict(self, X):
        predictions = self.model.predict(X)
        return tf.argmax(predictions, axis=1).numpy()

    def score(self, X, y):
        return self.model.evaluate(X, y, verbose=0)[1]

