import tensorflow as tf

class MyModel:
    def __init__(self, model):
        self.model = model

    def compile(self, loss, optimizer):
        self.model.compile(loss=loss, optimizer=optimizer)

    def fit(self, X, y, epochs, batch_size):
        self.model.fit(X, y, epochs=epochs, batch_size=batch_size)

    def evaluate(self, X, y):
        return self.model.evaluate(X, y)

    def predict(self, X):
        return self.model.predict(X)

    def save(self, filepath):
        self.model.save(filepath)

    def load(self, filepath):
        self.model.load_weights(filepath)

# Example usage
model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(128, activation='relu', input_shape=(784,)),
    tf.keras.layers.Dense(10, activation='softmax')
])

mymodel = MyModel(model)
mymodel.compile('categorical_cross entropy', 'adam')
mymodel.fit(..., epochs=10, batch_size=32)
