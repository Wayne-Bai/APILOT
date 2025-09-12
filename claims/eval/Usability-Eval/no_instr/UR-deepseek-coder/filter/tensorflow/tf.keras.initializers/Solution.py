import tensorflow as tf
from tensorflow.keras import initializers

# Define a custom initializer
class MyInitializer(initializers.Initializer):
    def __call__(self, shape, dtype=None):
        return tf.random.normal(shape, mean=0., stddev=1., dtype=dtype)

    def get_config(self):
        return {}

# Serialize the custom initializer
serialized_initializer = tf.keras.utils.serialize_keras_object(MyInitializer())

# Deserialize the custom initializer
deserialized_initializer = tf.keras.utils.deserialize_keras_object(serialized_initializer)

# Example usage in a model
model = tf.keras.Sequential([
    tf.keras.layers.Dense(64, kernel_initializer=deserialized_initializer, activation='relu'),
    tf.keras.layers.Dense(10, kernel_initializer=deserialized_initializer)
])

# Print the model summary to verify the initializers
model.summary()
