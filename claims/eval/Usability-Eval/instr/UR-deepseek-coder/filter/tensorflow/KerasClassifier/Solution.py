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

    def _build_model(self, input_dim, output_dim):
        model = Sequential()
        model.add(Dense(self.hidden_units, input_dim=input_dim, activation='relu'))
        model.add(Dense(output_dim, activation='softmax'))
        model.compile(optimizer=Adam(learning_rate=self.learning_rate),
                      loss='sparse_categorical_crossentropy',
                      metrics=['accuracy'])
        return model

    def fit(self, X, y):
        X, y = check_X_y(X, y)
        self.label_encoder.fit(y)
        y_encoded = self.label_encoder.transform(y)
        self.classes_ = self.label_encoder.classes_
        self.model = self._build_model(X.shape[1], len(self.classes_))
        self.model.fit(X, y_encoded, epochs=self.epochs, batch_size=self.batch_size, verbose=0)
        return self

    def predict(self, X):
        check_is_fitted(self)
        X = check_array(X)
        predictions = self.model.predict(X)
        return self.label_encoder.inverse_transform(np.argmax(predictions, axis=1))

    def predict_proba(self, X):
        check_is_fitted(self)
        X = check_array(X)
        return self.model.predict(X)
