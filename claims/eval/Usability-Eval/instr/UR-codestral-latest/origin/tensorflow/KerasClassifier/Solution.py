from abc import ABC, abstractmethod
import tensorflow as tf
from sklearn.base import BaseEstimator, ClassifierMixin

class TensorFlowClassifier(BaseEstimator, ClassifierMixin, ABC):
    def __init__(self, model, **hyperparameters):
        self.model = model
        self.hyperparameters = hyperparameters
        self.is_fitted = False

    def get_params(self, deep=True):
        return {"model": self.model, **self.hyperparameters}

    def set_params(self, **parameters):
        self.hyperparameters.update(parameters)
        return self

    def fit(self, X, y, **kwargs):
        self.model.compile(**self.hyperparameters)
        self.model.fit(X, y, **kwargs)
        self.is_fitted = True
        return self

    def predict(self, X, **kwargs):
        if not self.is_fitted:
            raise ValueError("Model is not fitted yet.")
        return tf.argmax(self.model.predict(X, **kwargs), axis=1).numpy()

    def score(self, X, y, **kwargs):
        if not self.is_fitted:
            raise ValueError("Model is not fitted yet.")
        predictions = self.predict(X, **kwargs)
        return (predictions == y).mean()
