import tensorflow as tf

class ModelHandler:
    def __init__(self, model, loss, optimizer, metrics):
        self.model = model
        self.loss = loss
        self.optimizer = optimizer
        self.metrics = metrics

    def train(self, train_dataset, epochs):
        self.model.compile(optimizer=self.optimizer, 
                           loss=self.loss, 
                           metrics=self.metrics)
        self.model.fit(train_dataset, epochs=epochs)

    def evaluate(self, test_dataset):
        return self.model.evaluate(test_dataset)

    def predict(self, data):
        return self.model.predict(data)

    def save_model(self, filepath):
        self.model.save(filepath)

    def load_model(self, filepath):
        self.model = tf.keras.models.load_model(filepath)

# Example usage:
# Create your model, dataset, and handle training/evaluation

# model = tf.keras.Sequential([...])
# handler = ModelHandler(model, loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
# handler.train(train_dataset, epochs=5)
# results = handler.evaluate(test_dataset)
# predictions = handler.predict(new_data)
# handler.save_model('my_model.h5')
