import tensorflow as tf
from sklearn.base import BaseEstimator, ClassifierMixin
from sklearn.utils.validation import check_X_y, check_array, check_is_fitted

class TensorFlowClassifier(BaseEstimator, ClassifierMixin):
    def __init__(self, input_dim, num_classes, hidden_units=[16, 16], learning_rate=0.01):
        self.input_dim = input_dim
        self.num_classes = num_classes
        self.hidden_units = hidden_units
        self.learning_rate = learning_rate

    def fit(self, X, y, epochs=100, batch_size=32):
        # Check that X and y have correct shape
        X, y = check_X_y(X, y)

        # Build the model
        self.model_ = self._build_model()

        # Convert labels to one-hot vector
        y_one_hot = tf.one_hot(y, self.num_classes)

        # Convert features to a tensor
        X_tensor = tf.convert_to_tensor(X, dtype=tf.float32)

        # Define loss and optimizer
        loss_object = tf.keras.losses.CategoricalCrossentropy()
        optimizer = tf.keras.optimizers.Adam(learning_rate=self.learning_rate)

        # Training loop
        for epoch in range(epochs):
            with tf.GradientTape() as tape:
                predictions = self.model_(X_tensor)
                loss = loss_object(y_one_hot, predictions)
            gradients = tape.gradient(loss, self.model_.trainable_variables)
            optimizer.apply_gradients(zip(gradients, self.model_.trainable_variables))

        return self

    def predict(self, X):
        # Check is fit had been called
        check_is_fitted(self)

        # Input validation
        X = check_array(X)

        # Convert features to a tensor
        X_tensor = tf.convert_to_tensor(X, dtype=tf.float32)

        predictions = self.model_(X_tensor)
        return tf.argmax(predictions, axis=1)

    def _build_model(self):
        model = tf.keras.models.Sequential()
        model.add(tf.keras.layers.InputLayer(input_shape=(self.input_dim,)))
        for units in self.hidden_units:
            model.add(tf.keras.layers.Dense(units, activation=tf.nn.relu))
        model.add(tf.keras.layers.Dense(self.num_classes))
        return model
