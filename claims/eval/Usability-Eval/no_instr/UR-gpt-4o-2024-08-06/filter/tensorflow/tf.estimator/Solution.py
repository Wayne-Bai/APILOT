import tensorflow as tf

class ModelManager:
    def __init__(self, model, optimizer, loss_fn, metrics=None):
        """
        Initializes the ModelManager with a given model and configurations.

        Args:
            model (tf.keras.Model): Keras model to manage.
            optimizer (tf.keras.optimizers.Optimizer): Optimizer for training.
            loss_fn (tf.keras.losses.Loss): Loss function for training.
            metrics (list): List of metrics to evaluate the model.
        """
        self.model = model
        self.model.compile(optimizer=optimizer, loss=loss_fn, metrics=metrics)

    def train(self, train_dataset, epochs, validation_data=None, callbacks=None):
        """
        Trains the model using the provided dataset.

        Args:
            train_dataset (tf.data.Dataset): Dataset for training.
            epochs (int): Number of epochs to train the model.
            validation_data (tf.data.Dataset, optional): Dataset for validation. Defaults to None.
            callbacks (list, optional): List of callbacks to be called during training. Defaults to None.
        
        Returns:
            history: A record of training loss values and metrics values at successive epochs.
        """
        history = self.model.fit(
            train_dataset,
            epochs=epochs,
            validation_data=validation_data,
            callbacks=callbacks
        )
        return history

    def evaluate(self, test_dataset):
        """
        Evaluates the model using the test dataset.

        Args:
            test_dataset (tf.data.Dataset): Dataset for evaluation.
        
        Returns:
            evaluation: The evaluation result as a list of scalars.
        """
        evaluation = self.model.evaluate(test_dataset)
        return evaluation

    def predict(self, input_data):
        """
        Makes predictions using the model.

        Args:
            input_data (tf.Tensor): Input data for making predictions.
        
        Returns:
            predictions: Model predictions.
        """
        predictions = self.model.predict(input_data)
        return predictions

    def export(self, export_path):
        """
        Exports the model to the specified path.

        Args:
            export_path (str): Path to save the model.
        """
        tf.keras.models.save_model(self.model, export_path)

# Example usage:
# Create a simple model for demonstration
def create_model(input_shape):
    model = tf.keras.Sequential([
        tf.keras.layers.InputLayer(input_shape=input_shape),
        tf.keras.layers.Dense(128, activation='relu'),
        tf.keras.layers.Dense(10, activation='softmax')
    ])
    return model

# Set up model details
input_shape = (28, 28)  # Example input shape for a simple NN
model = create_model(input_shape)

# Instantiate the ModelManager
manager = ModelManager(
    model=model,
    optimizer=tf.keras.optimizers.Adam(),
    loss_fn=tf.keras.losses.SparseCategoricalCrossentropy(),
    metrics=['accuracy']
)

# Example datasets
train_dataset = tf.data.Dataset.from_tensor_slices((tf.random.uniform([1000, 28, 28]), tf.random.uniform([1000], maxval=10, dtype=tf.int32))).batch(32)
test_dataset = tf.data.Dataset.from_tensor_slices((tf.random.uniform([200, 28, 28]), tf.random.uniform([200], maxval=10, dtype=tf.int32))).batch(32)

# Train the model
manager.train(train_dataset, epochs=5, validation_data=test_dataset)

# Evaluate the model
manager.evaluate(test_dataset)

# Predict using the model
dummy_input = tf.random.uniform([10, 28, 28])
predictions = manager.predict(dummy_input)
print(predictions)

# Export the model
manager.export('exported_model')
