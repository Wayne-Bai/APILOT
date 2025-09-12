import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn.base import BaseEstimator, ClassifierMixin

class TensorFlowClassifier(BaseEstimator, ClassifierMixin):
    def __init__(self, hidden_units=[16, 8], learning_rate=0.001, epochs=100):
        self.hidden_units = hidden_units
        self.learning_rate = learning_rate
        self.epochs = epochs

    def fit(self, X, y):
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        model = Sequential()
        model.add(Dense(self.hidden_units[0], input_dim=X.shape[1], activation='relu'))
        model.add(Dense(self.hidden_units[1], activation='relu'))
        model.add(Dense(1, activation='sigmoid'))

        model.compile(loss='binary_crossentropy', optimizer=tf.keras.optimizers.Adam(learning_rate=self.learning_rate), metrics=['accuracy'])

        model.fit(X_train, y_train, epochs=self.epochs, batch_size=32, verbose=1)

        self.model = model

    def predict(self, X):
        return self.model.predict(X)

    def score(self, X, y):
        return self.model.evaluate(X, y)[1]
