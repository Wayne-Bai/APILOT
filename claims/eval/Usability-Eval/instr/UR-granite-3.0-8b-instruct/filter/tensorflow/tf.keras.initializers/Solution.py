import tensorflow as tf

# Define a custom initializer
class CustomInitializer(tf.keras.initializers.Initializer):
    def __init__(self, value):
        self.value = value

    def __call__(self, shape, dtype=None):
        return tf.fill(shape, self.value)

# Serialize the initializer
serializer = tf.keras.initializers.serialization.serialize(CustomInitializer(5))
print(serializer)

# Deserialize the initializer
deserializer = tf.keras.initializers.serialization.deserialize(serializer)
print(deserializer(tf.TensorShape([3, 3])))
