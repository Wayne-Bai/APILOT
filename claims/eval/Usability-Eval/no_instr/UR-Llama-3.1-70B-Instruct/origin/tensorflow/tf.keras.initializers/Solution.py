import tensorflow as tf
from tensorflow.keras import layers
import json
import io

# Define a model with a layer that uses a custom initializer
class CustomInitializer(tf.keras.initializers.Initializer):
    def __init__(self):
        super(CustomInitializer, self).__init__()

    def __call__(self, shape, dtype=None, **kwargs):
        return tf.random.uniform(shape, maxval=1, dtype=dtype)

    def get_config(self):
        return {}

    @classmethod
    def from_config(cls, config):
        return cls()

model = tf.keras.models.Sequential([
    layers.Dense(10, kernel_initializer=CustomInitializer(), input_shape=(10,))
])

# Serialize the model's initializer
def serialize_initializer(initializer):
    config = initializer.get_config()
    return json.dumps(config)

initializer = model.layers[0].kernel_initializer
serialized_initializer = serialize_initializer(initializer)

# Deserialize the initializer
def deserialize_initializer(config_str):
    config = json.loads(config_str)
    return CustomInitializer().from_config(config)

deserialized_initializer = deserialize_initializer(serialized_initializer)

# Use the deserialized initializer to create a new layer
new_layer = layers.Dense(10, kernel_initializer=deserialized_initializer, input_shape=(10,))
new_model = tf.keras.models.Sequential([new_layer])

# Save the model to a file
with io.StringIO() as stream:
    new_model.to_yaml(stream)
    yaml_model = stream.getvalue()

# Load the model from the file
loaded_model = tf.keras.models.model_from_yaml(yaml_model)
loaded_model.summary()
