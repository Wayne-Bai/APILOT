
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

class TensorFlowClassifier(tf.keras.models.Model):
    def __init__(self, input_shape, output_dim):
        super(TensorFlowClassifier, self).__init__()
        self.input_layer = layers.Input(input_shape)
        self.dense1 = layers.Dense(64, activation='relu')(self.input_layer)
        self.dense2 = layers.Dense(32, activation='relu')(self.dense1)
        self.output_layer = layers.Dense(output_dim, activation='softmax')(self.dense2)
        self.model = keras.models.Model(inputs=self.input_layer, outputs=self.output_layer)

    def compile(self, optimizer, loss, metrics):
        self.optimizer = optimizer
        self.loss = loss
        self.metrics = metrics
        super(TensorFlowClassifier, self).compile()

    def fit(self, X_train, y_train, epochs=10, batch_size=32):
        self.model.fit(X_train, y_train, epochs=epochs, batch_size=batch_size)

    def evaluate(self, X_test, y_test):
        return self.model.evaluate(X_test, y_test)

    def predict(self, X_test):
        return self.model.predict(X_test)
