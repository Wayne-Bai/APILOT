import tensorflow as tf

# Example of creating a Keras initializer
initializer = tf.keras.initializers.RandomNormal(mean=0.0, stddev=0.05)

# Serialize the initializer
initializer_config = initializer.get_config()

# Deserialize the initializer
new_initializer = tf.keras.initializers.deserialize(initializer_config)

# Example usage of the new initializer in a layer
model = tf.keras.Sequential([
    tf.keras.layers.Dense(64, kernel_initializer=new_initializer, input_shape=(32,)),
    tf.keras.layers.Dense(10, kernel_initializer=new_initializer)
])

# Print model summary
model.summary()
