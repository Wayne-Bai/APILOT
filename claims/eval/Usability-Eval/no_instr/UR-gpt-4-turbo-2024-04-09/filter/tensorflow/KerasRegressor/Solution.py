import tensorflow as tf
from sklearn.base import BaseEstimator, ClassifierMixin
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn.metrics import accuracy_score

class TFClassifier(BaseEstimator, ClassifierMixin):
    def __init__(self, n_units=10, n_classes=2, epochs=100, learning_rate=0.01):
        """
        Initializes the TensorFlow Classifier.
        :param n_units: Number of units in the hidden layer
        :param n_classes: Number of output classes
        :param epochs: Number of epochs to train the model
        :param learning_rate: Learning rate for the optimizer
        """
        self.n_units = n_units
        self.n_classes = n_classes
        self.epochs = epochs
        self.learning_rate = learning_rate
        self.model = None

    def _build_model(self):
        # Build TensorFlow model
        self.model = Sequential([
            Dense(self.n_units, activation='relu', input_shape=(None,)),
            Dense(self.n_classes, activation='softmax')
        ])
        self.model.compile(optimizer=tf.optimizers.Adam(learning_rate=self.learning_rate),
                           loss='sparse_categorical_crossentropy',
                           metrics=['accuracy'])

    def fit(self, X, y):
        if self.model is None:
            self._build_model()
        # Train the model
        self.model.fit(X, y, epochs=self.epochs)

    def predict(self, X):
        # Make predictions
        if self.model is None:
            raise Exception("The model has not been trained yet. Please call `fit` first.")
        predictions = self.model.predict(X)
        return tf.argmax(predictions, axis=1).numpy()

    def score(self, X, y):
        # Compute accuracy of the model
        predictions = self.predict(X)
        return accuracy_score(y, predictions)

# Example usage
# Create an instance of the classifier
classifier = TFClassifier(n_units=10, n_classes=3, epochs=10)
# Assume X_train and y_train are available from your dataset
# classifier.fit(X_train, y_train)
# acc = classifier.score(X_train, y_train)
