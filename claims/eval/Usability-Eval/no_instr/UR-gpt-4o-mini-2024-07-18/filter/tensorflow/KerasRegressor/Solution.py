import tensorflow as tf
from sklearn.base import BaseEstimator, ClassifierMixin

class TensorFlowClassifier(BaseEstimator, ClassifierMixin):
    def __init__(self, model=None, epochs=10, batch_size=32):
        self.model = model
        self.epochs = epochs
        self.batch_size = batch_size

    def fit(self, X, y):
        # Convert inputs to TensorFlow tensors
        X_tensor = tf.convert_to_tensor(X, dtype=tf.float32)
        y_tensor = tf.convert_to_tensor(y, dtype=tf.float32)

        # Compile the model if not already compiled
        if not self.model:
            raise ValueError("No model provided to fit.")

        self.model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
        
        # Train the model
        self.model.fit(X_tensor, y_tensor, epochs=self.epochs, batch_size=self.batch_size)
        
        return self

    def predict(self, X):
        # Convert inputs to TensorFlow tensors
        X_tensor = tf.convert_to_tensor(X, dtype=tf.float32)
        predictions = self.model.predict(X_tensor)
        return tf.argmax(predictions, axis=1).numpy()

    def score(self, X, y):
        y_pred = self.predict(X)
        accuracy = tf.reduce_mean(tf.cast(tf.equal(y_pred, y), tf.float32)).numpy()
        return accuracy
