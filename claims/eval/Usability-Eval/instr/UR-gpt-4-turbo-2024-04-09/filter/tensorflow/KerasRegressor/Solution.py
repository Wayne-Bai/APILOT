import tensorflow as tf
from sklearn.base import BaseEstimator, ClassifierMixin
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.losses import SparseCategoricalCrossentropy

class TFClassifier(BaseEstimator, ClassifierMixin):
    def __init__(self, input_dim, output_dim, hidden_units=[64, 32], learning_rate=0.01):
        # Initialize the attributes
        self.input_dim = input_dim
        self.output_dim = output_dim
        self.hidden_units = hidden_units
        self.learning_rate = learning_rate
        self.model = self._build_model()

    def _build_model(self):
        # Build the TensorFlow model
        model = Sequential()
        model.add(Dense(self.hidden_units[0], activation='relu', input_shape=(self.input_dim,)))
        for units in self.hidden_units[1:]:
            model.add(Dense(units, activation='relu'))
        model.add(Dense(self.output_dim, activation='softmax'))
        return model

    def fit(self, X, y, epochs=100, batch_size=32):
        self.model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=self.learning_rate),
                           loss=SparseCategoricalCrossentropy(),
                           metrics=['accuracy'])
        self.model.fit(X, y, epochs=epochs, batch_size=batch_size)

    def predict(self, X):
        # Get the class with highest probability
        probabilities = self.model.predict(X)
        return tf.argmax(probabilities, axis=1)

    def score(self, X, y):
        # Evaluate the model and return the accuracy
        _, accuracy = self.model.evaluate(X, y, verbose=0)
        return accuracy
