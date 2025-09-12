import tensorflow as tf
from abc import ABC, abstractmethod

class AbstractOptimizer(ABC):

    @abstractmethod
    def get_config(self):
        """
        Returns the configuration of the optimizer as a Python dictionary.
        Must be implemented by subclasses.
        """
        pass

    @abstractmethod
    def apply_gradients(self, grads_and_vars):
        """
        Apply the given gradients to the respective variables.
        Must be implemented by subclasses.
        
        Args:
            grads_and_vars: list of (gradient, variable) pairs.
        """
        pass

class CustomOptimizer(AbstractOptimizer):
    def __init__(self, learning_rate=0.001):
        self.learning_rate = learning_rate

    def get_config(self):
        return {"learning_rate": self.learning_rate}

    def apply_gradients(self, grads_and_vars):
        for grad, var in grads_and_vars:
            if grad is not None:
                var.assign_sub(self.learning_rate * grad)

# Example usage:
optimizer = CustomOptimizer(learning_rate=0.01)

# Assume we have a simple linear model and a synthetic dataset
model = tf.keras.Sequential([tf.keras.layers.Dense(1)])
x = tf.constant([[1.0], [2.0], [3.0]])
y_true = tf.constant([[2.0], [4.0], [6.0]])

with tf.GradientTape() as tape:
    y_pred = model(x)
    loss = tf.reduce_mean(tf.square(y_true - y_pred))

grads = tape.gradient(loss, model.trainable_variables)
optimizer.apply_gradients(zip(grads, model.trainable_variables))

print("Model weights after one optimization step:", model.trainable_variables)
