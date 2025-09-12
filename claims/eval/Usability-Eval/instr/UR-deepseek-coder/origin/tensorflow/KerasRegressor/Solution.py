import tensorflow as tf
from sklearn.base import BaseEstimator, ClassifierMixin
from sklearn.utils.validation import check_X_y, check_array, check_is_fitted

class TensorFlowClassifier(BaseEstimator, ClassifierMixin):
    def __init__(self, n_hidden_units=100, n_classes=2, learning_rate=0.001, epochs=10):
        self.n_hidden_units = n_hidden_units
        self.n_classes = n_classes
        self.learning_rate = learning_rate
        self.epochs = epochs
        self.model = None

    def build_model(self, input_dim):
        model = tf.keras.Sequential([
            tf.keras.layers.Dense(self.n_hidden_units, input_dim=input_dim, activation='relu'),
            tf.keras.layers.Dense(self.n_classes, activation='softmax')
        ])
        model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=self.learning_rate),
                      loss='sparse_categorical_crossentropy',
                      metrics=['accuracy'])
        return model

    def fit(self, X, y):
        X, y = check_X_y(X, y)
        self.model = self.build_model(input_dim=X.shape[1])
        self.model.fit(X, y, epochs=self.epochs, verbose=0)
        return self

    def predict(self, X):
        check_is_fitted(self)
        X = check_array(X)
        predictions = self.model.predict(X)
        return predictions.argmax(axis=1)

    def score(self, X, y):
        X, y = check_X_y(X, y)
        loss, accuracy = self.model.evaluate(X, y, verbose=0)
        return accuracy
