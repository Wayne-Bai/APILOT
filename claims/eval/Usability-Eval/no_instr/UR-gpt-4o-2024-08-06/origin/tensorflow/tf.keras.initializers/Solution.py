import tensorflow as tf

# Create an initializer instance
initializer = tf.keras.initializers.GlorotUniform()

# Serialize the initializer to a JSON-serializable dict
initializer_config = tf.keras.initializers.serialize(initializer)

# Print serialized initializer
print("Serialized Initializer:", initializer_config)

# Deserialize the initializer from the serialized configuration
deserialized_initializer = tf.keras.initializers.deserialize(initializer_config)

# Verify that deserialization gives us the same type of initializer
print("Deserialized Initializer:", type(deserialized_initializer))
