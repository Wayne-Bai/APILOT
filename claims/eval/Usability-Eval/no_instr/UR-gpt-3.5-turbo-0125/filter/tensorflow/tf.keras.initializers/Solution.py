
import tensorflow as tf

class MyInitializer(tf.keras.initializers.Initializer):
    def __init__(self, seed=None):
        self.seed = seed

    def __call__(self, shape, dtype=None):
        return tf.random.normal(shape, seed=self.seed)

    def get_config(self):
        return {'seed': self.seed}

# Example of serializing and deserializing the custom initializer
initializer = MyInitializer(seed=42)

config = initializer.get_config()
reconstructed_initializer = MyInitializer(**config)

print(initializer(seed=42))
print(reconstructed_initializer(seed=42))
