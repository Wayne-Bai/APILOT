import tensorflow as tf
from sklearn.base import ClassifierMixin

class TensorFlowClassifier(ClassifierMixin):
    def __init__(self, model):
        self.model = model
        self._estimator = None

    def fit(self, X, y):
        self._estimator = tf.keras.Model(self.model, compile=True, loss='categorical_crossentropy')
        self._estimator.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

        for epoch in range(10):
            self._estimator.fit(X, y, epochs=1)

    def predict(self, X):
        return self.model.predict(X)
