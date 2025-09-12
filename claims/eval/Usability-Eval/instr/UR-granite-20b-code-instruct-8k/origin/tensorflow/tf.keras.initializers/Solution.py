import tensorflow as tf

# Define a Keras initializer
initializer = tf.keras.initializers. glorot_uniform()

# Serialize the Keras initializer
initializer_config = initializer.get_config()
initializer_json = tf.keras.utils.serialize_keras_object(initializer)

# Deserialize the Keras initializer
deserialized_initializer = tf.keras.initializers.deserialize(initializer_json)

# Check if the deserialized initializer is the same as the original initializer
assert isinstance(deserialized_initializer, tf.keras.initializers.GlorotUniform)
assert deserialized_initializer.get_config() == initializer_config
