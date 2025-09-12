import tensorflow as tf
import numpy as np
from sklearn.base import BaseEstimator, ClassifierMixin

class TFClassifier(BaseEstimator, ClassifierMixin):
    def __init__(self, input_shape, num_classes, epochs=10, batch_size=32, learning_rate=0.001):
        self.input_shape = input_shape
        self.num_classes = num_classes
        self.epochs = epochs
        self.batch_size = batch_size
        self.learning_rate = learning_rate

        self.model = self._build_model()

    def _build_model(self):
        model = tf.keras.Sequential([
            tf.keras.layers.Flatten(input_shape=self.input_shape),
            tf.keras.layers.Dense(128, activation='relu'),
            tf.keras.layers.Dense(self.num_classes, activation='softmax')
        ])
        
        model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=self.learning_rate),
                      loss='sparse_categorical_crossentropy',
                      metrics=['accuracy'])
        return model

    def fit(self, X, y):
        self.model.fit(X, y, epochs=self.epochs, batch_size=self.batch_size)
        return self

    def predict(self, X):
        predictions = self.model.predict(X)
        return np.argmax(predictions, axis=1)

    def score(self, X, y):
        loss, accuracy = self.model.evaluate(X, y)
        return accuracy

# Example usage:
# classifier = TFClassifier(input_shape=(28, 28), num_classes=10)
# classifier.fit(train_images, train_labels)
# accuracy = classifier.score(test_images, test_labels)
