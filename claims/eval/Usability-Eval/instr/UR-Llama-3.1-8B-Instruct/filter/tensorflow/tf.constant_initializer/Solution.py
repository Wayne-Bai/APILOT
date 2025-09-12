# Import the necessary library
import tensorflow as tf

class ConstantInitializer(tf.keras.initializers.Initializer):
    """
    Custom initializer that generates tensors with constant values.
    """
    
    def __init__(self, constant_value):
        """
        Args:
            constant_value (float): The constant value to initialize the tensor with.
        """
        self.constant_value = constant_value

    def __call__(self, shape, dtype=None):
        """
        Args:
            shape (tuple): The shape of the tensor to initialize.
            dtype (optional): The data type of the tensor to initialize. Defaults to None.
        Returns:
            tf.Tensor: The initialized tensor with the constant value.
        """
        if dtype is None:
            dtype = tf.float32
        return tf.fill(shape, self.constant_value)

modelelement = [64, 8, 2, 1]
model_weights_initializer = ConstantInitializer(0.0)

#Example usage:
model = tf.keras.Sequential([
    tf.keras.layers.Dense(units=64, kernel_initializer=model_weights_initializer, input_shape=(modelelement[0],))
])

#Test the model
model.summary()
