import tensorflow as tf

class SklearnRegressorMixin(tf.keras.Model):

    def __init__(self, model, **kwargs):
        super().__init__(**kwargs)
        self.model = model

    def call(self, x):
        return self.model(x)

    def fit(self, x, y, **kwargs):
        self.model.fit(x, y, **kwargs)

    def predict(self, x):
        return self.model.predict(x)

    def score(self, x, y):
        return self.model.evaluate(x, y)
