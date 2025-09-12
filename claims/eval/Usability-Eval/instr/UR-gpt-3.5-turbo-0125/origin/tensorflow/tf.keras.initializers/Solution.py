
import tensorflow as tf
from tensorflow.python.ops import init_ops

class MyCustomInitializer(init_ops.Initializer):
    def __init__(self, param1, param2):
        self.param1 = param1
        self.param2 = param2

    def __call__(self, shape, dtype=tf.float32):
        # Custom initialization logic here
        return tf.random.uniform(shape, minval=self.param1, maxval=self.param2, dtype=dtype)

    def get_config(self):
        return {'param1': self.param1, 'param2': self.param2}

# Usage example
initializer = MyCustomInitializer(param1=0, param2=1)

# Serialize the initializer
config = tf.keras.initializers.serialize(initializer)

# Deserialize the initializer
reconstructed_initializer = tf.keras.initializers.deserialize(config)
