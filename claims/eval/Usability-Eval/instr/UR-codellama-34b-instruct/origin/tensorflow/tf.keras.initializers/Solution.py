
import tensorflow as tf
from tensorflow.keras import initializers

# Define an example initializer
initializer = initializers.RandomNormal(mean=0, stddev=1)

# Serialize the initializer to JSON
serialized_initializer = json.dumps(initializer.get_config())

# Deserialize the initializer from JSON
deserialized_initializer = tf.keras.initializers.deserialize(serialized_initializer)
