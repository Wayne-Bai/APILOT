import tensorflow as tf
from sklearn.base import BaseEstimator, ClassifierMixin
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.losses import SparseCategoricalCrossentropy

class TFClassifier(BaseEstimator, ClassifierMixin):
    def __init__(self, units=10, activation='relu', optimizer='adam', epochs=10):
        # Initializes the classifier with the structure and training parameters
        self.units = units
        self.activation = activation
        self.optimizer = optimizer
        self.epochs = epochs
        self.model = Sequential([
            Dense(units=self.units, activation=self.activation, input_dim=2),  # Adjust input_dim as per your feature size
            Dense(units=3, activation='softmax')  # Adjust units as per number of classes (output)
        ])
    
    def fit(self, X, y):
        # Compiles and fits the model
        self.model.compile(optimizer=self.optimizer, loss=SparseCategoricalCrossentropy(from_logits=False), metrics=['accuracy'])
        self.model.fit(X, y, epochs=self.epochs)
        return self
    
    def predict(self, X):
        # Uses the trained model to make predictions
        predictions = self.model.predict(X)
        return tf.argmax(predictions, axis=1).numpy()
    
    def score(self, X, y):
        # Evaluates the model on the provided test data and labels
        loss, accuracy = self.model.evaluate(X, y)
        return accuracy

# Example usage:
# Assuming you have loaded your data into train_X, train_y, test_X, testy_y
# You might need to encode labels to start from 0 and may need to reshape inputs as necessary

# classifier = TFClassifier(units=10, activation='relu', optimizer='adam', epochs=20)
# classifier.fit(train_X, train_y)
# accuracy = classifier.score(test_X, test_y)
# print("Model accuracy: {:.2f}%".format(accuracy * 100))
