import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam
from sklearn.base import BaseEstimator, ClassifierMixin
from sklearn.utils.validation import check_X_y, check_array, check_is_fitted
from sklearn.preprocessing import LabelEncoder
import numpy as np

class TensorFlowClassifier(BaseEstimator, ClassifierMixin):
    def __init__(self, hidden_units=10, learning_rate=0.001, epochs=10, batch_size=32):
        self.hidden_units = hidden_units
        self.learning_rate = learning_rate
        self.epochs = epochs
        self.batch_size = batch_size
        self.model = None
        self.label_encoder = LabelEncoder()

    def fit(self, X, y):
        X, y = check_X_y(X, y)
        y = self.label_encoder.fit_transform(y)
        num_classes = len(self.label_encoder.classes_)

        self.model = Sequential([
            Dense(self.hidden_units, activation='relu', input_shape=(X.shape[1],)),
            Dense(num_classes, activation='softmax')
        ])

        self.model.compile(optimizer=Adam(learning_rate=self.learning_rate),
                           loss='sparse_categorical_crossentropy',
                           metrics=['accuracy'])

        self.model.fit(X, y, epochs=self.epochs, batch_size=self.batch_size, verbose=0)
        return self

    def predict(self, X):
        check_is_fitted(self)
        X = check_array(X)
        predictions = self.model.predict(X, verbose=0)
        return self.label_encoder.inverse_transform(np.argmax(predictions, axis=1))

    def predict_proba(self, X):
        check_is_fitted(self)
        X = check_array(X)
        return self.model.predict(X, verbose=0)
