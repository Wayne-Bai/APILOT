import tensorflow as tf
from sklearn.base import BaseEstimator, ClassifierMixin

class TensorFlowClassifier(BaseEstimator, ClassifierMixin):
    def __init__(self, model, epochs=10, batch_size=32):
        self.model = model
        self.epochs = epochs
        self.batch_size = batch_size
        self.is_fitted_ = False

    def fit(self, X, y):
        self.model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
        self.model.fit(X, y, epochs=self.epochs, batch_size=self.batch_size)
        self.is_fitted_ = True
        return self

    def predict(self, X):
        if not self.is_fitted_:
            raise RuntimeError("You must fit the model before calling predict.")
        predictions = self.model.predict(X)
        return tf.argmax(predictions, axis=1).numpy()

    def score(self, X, y):
        if not self.is_fitted_:
            raise RuntimeError("You must fit the model before calling score.")
        loss, accuracy = self.model.evaluate(X, y)
        return accuracy

# Example of how to use the TensorFlowClassifier
# Define a simple model
def create_model(input_shape, num_classes):
    model = tf.keras.Sequential([
        tf.keras.layers.Input(shape=input_shape),
        tf.keras.layers.Dense(128, activation='relu'),
        tf.keras.layers.Dense(num_classes, activation='softmax')
    ])
    return model

# Usage
# model = create_model(input_shape=(28, 28), num_classes=10)
# clf = TensorFlowClassifier(model=model, epochs=5)
# clf.fit(X_train, y_train)
# predictions = clf.predict(X_test)
# accuracy = clf.score(X_test, y_test)
