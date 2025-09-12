import tensorflow as tf

# Define a custom initializer
class MyCustomInitializer(tf.keras.initializers.Initializer):
    def __init__(self, factor=1.0):
        super(MyCustomInitializer, self).__init__()
        self.factor = factor

    def __call__(self, shape, dtype=None):
        return self.factor * tf.random.normal(shape, dtype=dtype)

    def get_config(self):
        return {"factor": self.factor}

# Serialize the initializer
initializer = MyCustomInitializer(factor=0.5)
config = initializer.get_config()

# Save the config as a JSON string
json_string = tf.keras.initializers.serialize(initializer)

# Deserialize the JSON back to a Keras initializer object
initializer_deserialized = tf.keras.initializers.deserialize(json_string)

print("Original:", initializer)
print("Serialized:", json_string)
print("Deserialized:", initializer_deserialized)
