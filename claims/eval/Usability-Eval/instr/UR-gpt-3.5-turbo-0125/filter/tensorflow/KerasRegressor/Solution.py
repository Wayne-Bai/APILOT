
import tensorflow as tf
from sklearn.base import BaseEstimator

class TensorFlowRegressor(BaseEstimator):
    def __init__(self, num_features, num_hidden_units):
        self.num_features = num_features
        self.num_hidden_units = num_hidden_units
        self.weights = None
        self.biases = None
        self.optimizer = tf.keras.optimizers.Adam()

    def fit(self, X, y, epochs=100, learning_rate=0.01):
        self.weights = tf.Variable(tf.random.normal([self.num_features, self.num_hidden_units]))
        self.biases = tf.Variable(tf.zeros([self.num_hidden_units]))

        for epoch in range(epochs):
            with tf.GradientTape() as tape:
                hidden = tf.nn.relu(tf.add(tf.matmul(X, self.weights), self.biases))
                y_pred = tf.squeeze(tf.layers.dense(hidden, 1))
                loss = tf.losses.mean_squared_error(y, y_pred)
            gradients = tape.gradient(loss, [self.weights, self.biases])
            self.optimizer.apply_gradients(zip(gradients, [self.weights, self.biases]))

    def predict(self, X):
        hidden = tf.nn.relu(tf.add(tf.matmul(X, self.weights), self.biases))
        y_pred = tf.squeeze(tf.layers.dense(hidden, 1))
        return y_pred
