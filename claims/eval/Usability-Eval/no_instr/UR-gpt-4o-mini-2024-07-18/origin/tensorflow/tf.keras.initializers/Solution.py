import tensorflow as tf

# Example of a Keras initializer
initializer = tf.keras.initializers.RandomNormal(mean=0.0, stddev=0.05)

# Serialize the initializer to a JSON-compatible format
serializable_initializer = {
    'class_name': initializer.__class__.__name__,
    'config': initializer.get_config()
}

# Serialize to JSON string
import json
initializer_json = json.dumps(serializable_initializer)

print("Serialized initializer:", initializer_json)

# Deserialize the JSON back to an initializer
initializer_config = json.loads(initializer_json)
deserialized_initializer = tf.keras.initializers.get(initializer_config)

# Verify the deserialized initializer
print("Deserialized initializer:", deserialized_initializer)
