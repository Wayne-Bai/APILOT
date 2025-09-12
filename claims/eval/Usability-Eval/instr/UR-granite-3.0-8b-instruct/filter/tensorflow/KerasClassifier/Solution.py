import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn.base import ClassifierMixin

class TensorFlowClassifier(ClassifierMixin):
    def __init__(self, input_dim, hidden_dim, output_dim, learning_rate=0.01):
        self.input_dim = input_dim
        self.hidden_dim = hidden_dim
        self.output_dim = output_dim
        self.learning_rate = learning_rate

        self.model = self.build_model()

    def build_model(self):
        model = Sequential()
        model.add(Dense(self.hidden_dim, activation='relu', input_dim=self.input_dim))
        model.add(Dense(self.output_dim, activation='softmax'))

        model.compile(optimizer=tf.keras.optimizers.Adam(self.learning_rate),
                      loss='categorical_crossentropy',
                      metrics=['accuracy'])

        return model

    def fit(self, X, y):
        self.model.fit(X, y, epochs=10, batch_size=32, verbose=1)

    def predict(self, X):
        return self.model.predict(X)
