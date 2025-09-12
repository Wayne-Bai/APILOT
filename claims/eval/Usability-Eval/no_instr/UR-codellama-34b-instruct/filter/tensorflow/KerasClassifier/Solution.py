
import tensorflow as tf
from tensorflow import keras
from sklearn.base import ClassifierMixin

class TensorFlowClassifier(keras.Model, ClassifierMixin):
    def __init__(self, model, input_shape=(None, 1), n_classes=2, activation='softmax'):
        super().__init__()
        self.model = model
        self.input_shape = input_shape
        self.n_classes = n_classes
        self.activation = activation
        
    def fit(self, X, y):
        # Convert data to tensors
        X_tensor = tf.convert_to_tensor(X)
        y_tensor = tf.convert_to_tensor(y)
        
        # Flatten the input data if necessary
        if len(X_tensor.shape) > 2:
            X_tensor = tf.reshape(X_tensor, (X_tensor.shape[0], -1))
            
        # Compile the model with the specified loss function and optimizer
        self.model.compile(loss=tf.keras.losses.BinaryCrossentropy(), optimizer='adam')
        
        # Fit the model to the data
        self.model.fit(X_tensor, y_tensor)
        
    def predict(self, X):
        # Convert data to tensors
        X_tensor = tf.convert_to_tensor(X)
        
        # Flatten the input data if necessary
        if len(X_tensor.shape) > 2:
            X_tensor = tf.reshape(X_tensor, (X_tensor.shape[0], -1))
            
        # Use the model to make predictions on the data
        y_pred = self.model.predict(X_tensor)
        
        return y_pred
