import tensorflow as tf

class CustomInitializer(tf.keras.initializers.Initializer):
    def __call__(self, shape, dtype=None):
        # Custom initialization logic here
        return tf.random.normal(shape, mean=0.0, stddev=1.0)

# Serialize the initializer
initializer = CustomInitializer()
serialized_initializer = tf.keras.initializers.serialize(initializer)

# Deserialize the initializer
deserialized_initializer = tf.keras.initializers.deserialize(serialized_initializer, custom_objects={'CustomInitializer': CustomInitializer})

# Now you can use the deserialized initializer in your layers
layer = tf.keras.layers.Dense(10, kernel_initializer=deserialized_initializer)
