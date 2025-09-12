import tensorflow as tf

class TFClassifier(tf.Module, sklearn.base.ClassifierMixin):
    def __init__(self, model):
        super().__init__()
        self.model = model

    def fit(self, X, y):
        self.trained_weights = self.model.trainable_variables
        history = self.model.fit(X, y, epochs=10)
        return history

    def predict(self, X):
        return tf.argmax(self.model.predict(X), axis=1).numpy()

    def score(self, X, y):
        return self.model.evaluate(X, y)[1]

    def serialize(self):
        tf.saved_model.save(self.model, "./saved_model")

    def deserialize(self):
        loaded_model = tf.saved_model.load("./saved_model")
        self.model = loaded_model
