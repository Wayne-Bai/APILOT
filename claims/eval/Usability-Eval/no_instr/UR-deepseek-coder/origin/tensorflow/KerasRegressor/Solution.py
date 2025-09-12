import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam
from sklearn.base import BaseEstimator, ClassifierMixin
from sklearn.utils.validation import check_X_y, check_array, check_is_fitted

class TensorFlowClassifier(BaseEstimator, ClassifierMixin):
    def __init__(self, hidden_units=10, learning_rate=0.001, epochs=10, batch_size=32):
        self.hidden_units = hidden_units
        self.learning_rate = learning_rate
        self.epochs = epochs
        self.batch_size = batch_size
        self.model = None

    def build_model(self, input_dim):
        model = Sequential()
        model.add(Dense(self.hidden_units, input_dim=input_dim, activation='relu'))
        model.add(Dense(1, activation='sigmoid'))
        model.compile(optimizer=Adam(learning_rate=self.learning_rate), loss='binary_crossentropy', metrics=['accuracy'])
        return model

    def fit(self, X, y):
        X, y = check_X_y(X, y)
        self.model = self.build_model(X.shape[1])
        self.model.fit(X, y, epochs=self.epochs, batch_size=self.batch_size, verbose=0)
        return self

    def predict(self, X):
        check_is_fitted(self, 'model')
        X = check_array(X)
        return (self.model.predict(X) > 0.5).astype(int)

    def score(self, X, y):
        X, y = check_X_y(X, y)
        loss, accuracy = self.model.evaluate(X, y, verbose=0)
        return accuracy
