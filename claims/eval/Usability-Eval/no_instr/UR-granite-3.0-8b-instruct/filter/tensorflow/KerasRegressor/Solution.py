import tensorflow as tf
from tensorflow import keras
from sklearn.base import BaseEstimator

class TensorFlowClassifier(BaseEstimator, keras.Model):
    def __init__(self, input_dim, num_classes, learning_rate=0.001):
        super(TensorFlowClassifier, self).__init__()
        self.input_dim = input_dim
        self.num_classes = num_classes
        self.learning_rate = learning_rate

        self.model = keras.Sequential([
            keras.layers.Dense(64, activation='relu', input_shape=(input_dim,)),
            keras.layers.Dense(64, activation='relu'),
            keras.layers.Dense(num_classes, activation='softmax')
        ])

        self.optimizer = tf.keras.optimizers.Adam(learning_rate=self.learning_rate)
        self.loss_object = tf.keras.losses.SparseCategoricalCrossentropy()
        self.metric = tf.keras.metrics.SparseCategoricalAccuracy()

    def call(self, inputs):
        return self.model(inputs)

    def train_step(self, inputs, targets):
        with tf.GradientTape() as tape:
            predictions = self.model(inputs, training=True)
            loss = self.loss_object(targets, predictions)
        gradients = tape.gradient(loss, self.model.trainable_variables)
        self.optimizer.apply_gradients(zip(gradients, self.model.trainable_variables))
        self.metric.update_state(targets, predictions)
        return {'loss': loss, 'accuracy': self.metric.result()}

    def test_step(self, inputs, targets):
        predictions = self.model(inputs, training=False)
        loss = self.loss_object(targets, predictions)
        self.metric.update_state(targets, predictions)
        return {'loss': loss, 'accuracy': self.metric.result()}

    def predict(self, inputs):
        return self.model(inputs, training=False)
