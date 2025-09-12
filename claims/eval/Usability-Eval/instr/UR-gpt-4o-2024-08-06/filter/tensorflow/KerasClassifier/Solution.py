import tensorflow as tf
from sklearn.base import ClassifierMixin, BaseEstimator
import numpy as np

class TensorFlowClassifier(ClassifierMixin, BaseEstimator):
    def __init__(self, input_shape, num_classes, epochs=10, batch_size=32):
        self.input_shape = input_shape
        self.num_classes = num_classes
        self.epochs = epochs
        self.batch_size = batch_size
        
        # Define a simple Sequential model
        self.model = tf.keras.Sequential([
            tf.keras.layers.InputLayer(input_shape=self.input_shape),
            tf.keras.layers.Dense(128, activation='relu'),
            tf.keras.layers.Dense(64, activation='relu'),
            tf.keras.layers.Dense(self.num_classes, activation='softmax')
        ])
        
        # Compile the model
        self.model.compile(
            loss='sparse_categorical_crossentropy',
            optimizer=tf.keras.optimizers.Adam(),
            metrics=['accuracy']
        )
    
    def fit(self, X, y):
        # Train the model
        self.model.fit(X, y, epochs=self.epochs, batch_size=self.batch_size)
        return self
    
    def predict(self, X):
        # Predict classes
        y_pred = self.model.predict(X)
        return np.argmax(y_pred, axis=1)
    
    def predict_proba(self, X):
        # Predict probabilities
        return self.model.predict(X)

    def score(self, X, y):
        # Evaluate accuracy of the model
        score = self.model.evaluate(X, y, verbose=0)
        return score[1]

# Example usage
# clf = TensorFlowClassifier(input_shape=(784,), num_classes=10)
# clf.fit(train_data, train_labels)
# accuracy = clf.score(test_data, test_labels)
# print(f"Accuracy: {accuracy}")
