import tensorflow as tf
import numpy as np
from sklearn.base import BaseEstimator, RegressorMixin
from sklearn.utils.validation import check_X_y, check_array, check_is_fitted

class TensorFlowRegressor(BaseEstimator, RegressorMixin):
    def __init__(self, learning_rate=0.01, epochs=1000):
        self.learning_rate = learning_rate
        self.epochs = epochs
        self.model = None

    def fit(self, X, y):
        X, y = check_X_y(X, y)
        self.input_shape_ = X.shape[1]

        # Define a simple Sequential model
        self.model = tf.keras.models.Sequential([
            tf.keras.layers.Dense(64, activation='relu', input_shape=(self.input_shape_,)),
            tf.keras.layers.Dense(1, activation='linear')
        ])
        
        # Compile the model
        self.model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=self.learning_rate),
                           loss='mean_squared_error')

        # Fit the model
        self.model.fit(X, y, epochs=self.epochs, verbose=0)
        return self

    def predict(self, X):
        check_is_fitted(self)
        X = check_array(X)

        # Predict using the trained model
        y_pred = self.model.predict(X)
        return y_pred.flatten()

    def get_params(self, deep=True):
        return {"learning_rate": self.learning_rate, "epochs": self.epochs}
    
    def set_params(self, **params):
        for param, value in params.items():
            setattr(self, param, value)
        return self
