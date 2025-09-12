import tensorflow as tf
from sklearn.base import RegressorMixin, BaseEstimator
from sklearn.datasets import make_regression

class TensorFlowRegressor(BaseEstimator, RegressorMixin):
    def __init__(self, learning_rate=0.01, epochs=100):
        self.learning_rate = learning_rate
        self.epochs = epochs

    def fit(self, X, y):
        # Define the input placeholder
        self.X = tf.placeholder(tf.float32, shape=(None, X.shape[1]))
        self.y = tf.placeholder(tf.float32, shape=(None, ))

        # Define weights and biases
        self.weights = tf.Variable(tf.random_normal([X.shape[1], 1]))
        self.biases = tf.Variable(tf.zeros([1]))

        # Define our linear model
        pred = tf.matmul(self.X, self.weights) + self.biases

        # Define loss and optimization operations
        self.loss = tf.reduce_mean(tf.square(y - pred))
        optimizer = tf.train.GradientDescentOptimizer(learning_rate=self.learning_rate).minimize(self.loss)

        # Initialize variables
        self.sess = tf.Session()
        self.sess.run(tf.global_variables_initializer())

        # Train the model
        for _ in range(self.epochs):
            self.sess.run(optimizer, feed_dict={self.X: X, self.y: y})

    def predict(self, X):
        # Make predictions
        pred = self.sess.run(tf.matmul(self.X, self.weights) + self.biases, feed_dict={self.X: X})
        return pred.flatten()

# Test the model
X, y = make_regression(n_samples=100, n_features=1, noise=0.1)
model = TensorFlowRegressor()
model.fit(X, y)
print(model.predict(X))
