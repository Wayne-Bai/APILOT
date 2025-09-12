import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.losses import SparseCategoricalCrossentropy
from sklearn.base import ClassifierMixin, BaseEstimator

class CustomClassifier(ClassifierMixin, BaseEstimator):
    def __init__(self):
        self.model = None

    def fit(self, X, y):
        # Define the model
        self.model = Sequential([
            Dense(10, activation='relu', input_shape=(X.shape[1],)),
            Dense(10, activation='relu'),
            Dense(1, activation='sigmoid')
        ])

        # Compile the model
        self.model.compile(optimizer='adam', loss=SparseCategoricalCrossentropy(),
                          metrics=['accuracy'])

        # Fit the model to the data
        self.model.fit(X, y, epochs=10, batch_size=32, verbose=0)

        return self

    def predict(self, X):
        return (self.model.predict(X) > 0.5).astype(int)

    def predict_proba(self, X):
        return self.model.predict(X)
