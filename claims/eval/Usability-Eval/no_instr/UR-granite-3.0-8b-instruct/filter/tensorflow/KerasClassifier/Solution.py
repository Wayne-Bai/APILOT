import tensorflow as tf
from tensorflow import keras
from sklearn.base import ClassifierMixin

class TensorFlowClassifier(keras.Model, ClassifierMixin):
    def __init__(self, num_classes):
        super(TensorFlowClassifier, self).__init__()
        self.num_classes = num_classes
        self.dense1 = keras.layers.Dense(64, activation='relu')
        self.dense2 = keras.layers.Dense(64, activation='relu')
        self.dense3 = keras.layers.Dense(num_classes, activation='softmax')

    def call(self, inputs):
        x = self.dense1(inputs)
        x = self.dense2(x)
        return self.dense3(x)

    def fit(self, x_train, y_train, epochs=10, batch_size=32):
        self.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
        self.fit(x_train, y_train, epochs=epochs, batch_size=batch_size)

    def predict(self, x_test):
        return self.predict(x_test)

    def predict_proba(self, x_test):
        return self.predict(x_test)
