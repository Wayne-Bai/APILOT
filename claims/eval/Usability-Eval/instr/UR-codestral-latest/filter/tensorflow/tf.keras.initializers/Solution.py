import tensorflow as tf
import json

# Create a custom initializer
initializer = tf.keras.initializers.RandomNormal(mean=0., stddev=1.)
# Use it to create a variable
variables = tf.Variable(initializer(shape=(10, 10)))

# Save the configuration of the initializer
initializer_config = initializer.get_config()

# Save it to JSON format
with open('initializer.json', 'w') as fp:
    json.dump(initializer_config, fp)

# Load the configuration from saved file
with open('initializer.json', 'r') as fp:
    restored_config = json.load(fp)

# Recreate the initializer from configuration
restored_initializer = tf.keras.initializers.get(restored_config)

# Use the restored initializer for another variable
another_variable = tf.Variable(restored_initializer(shape=(20, 20)))
