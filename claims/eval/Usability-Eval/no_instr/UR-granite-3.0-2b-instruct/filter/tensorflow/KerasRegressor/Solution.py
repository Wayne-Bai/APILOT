import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

class TensorFlowClassifier(tf.keras.models.RegressorMixin):
    def __init__(self, hidden_units=10, output_units=1, activation='relu'):
        super(TensorFlowClassifier, self).__init__()
        self.hidden_units = hidden_units
        self.output_units = output_units
        self.activation = activation

        self.model = Sequential()
        self.model.add(Dense(hidden_units, input_dim=self.input_dim, activation=self.activation))
        self.model.add(Dense(output_units, activation='sigmoid'))

    def fit(self, X, y, epochs=100, batch_size=32):
        self.model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
        self.model.fit(X, y, epochs=epochs, batch_size=batch_size)

    def predict(self, X):
        return self.model.predict(X)

    def score(self, X, y):
        y_pred = self.predict(X)
        return accuracy_score(y, (y_pred > 0.5))
