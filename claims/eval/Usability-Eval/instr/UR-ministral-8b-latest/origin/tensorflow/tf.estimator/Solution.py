import tensorflow as tf

class ModelTrainingPipeline:
    def __init__(self, model, loss_function=tf.keras.losses.MeanSquaredError,
                 optimizer=tf.keras.optimizers.Adam, metrics=['accuracy']):
        self.model = model
        self.loss_function = loss_function
        self.optimizer = optimizer
        self.metrics = metrics

    def compile(self):
        self.model.compile(optimizer=self.optimizer, loss=self.loss_function,
                          metrics=self.metrics)

    def fit(self, x, y, epochs=10, batch_size=32):
        self.model.fit(x, y, epochs=epochs, batch_size=batch_size)

    def evaluate(self, x, y):
        return self.model.evaluate(x, y)

    def predict(self, x):
        return self.model.predict(x)

    def save(self, filepath):
        self.model.save(filepath)

# Example usage:
# Create a simple model
model = tf.keras.Sequential([
    tf.keras.layers.Dense(10, activation='relu', input_shape=(20,)),
    tf.keras.layers.Dense(1)
])

# Initialize the training pipeline
training_pipeline = ModelTrainingPipeline(model)
training_pipeline.compile()

# Dummy data
train_data = tf.data.Dataset.from_tensor_slices((tf.random.uniform([100, 20]), tf.random.uniform([100, 1])))
validation_data = tf.data.Dataset.from_tensor_slices((tf.random.uniform([20, 20]), tf.random.uniform([20, 1])))

# Fit the model
training_pipeline.fit(train_data, epochs=5)

# Evaluate the model
loss, accuracy = training_pipeline.evaluate(train_data)
print(f'Validation loss: {loss}, Validation accuracy: {accuracy}')

# Make predictions
predictions = training_pipeline.predict(train_data)
print(predictions)

# Save the model
training_pipeline.save("saved_model")
