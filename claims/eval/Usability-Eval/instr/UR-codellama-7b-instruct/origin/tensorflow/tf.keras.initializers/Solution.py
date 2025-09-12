
import json
from keras import models
from keras import layers
from keras.utils import serialize_keras_object
from keras.utils import deserialize_keras_object

# Define a simple Keras model
model = Sequential()
model.add(layers.Dense(64, activation='relu', input_shape=(784,)))
model.add(layers.Dense(10, activation='softmax'))

# Serialize the model using `serialize_keras_object`
serialized = serialize_keras_object(model)
print(json.dumps(serialized, indent=2))

# Deserialize the model using `deserialize_keras_object`
deserialized_dict = json.loads(serialized)
deserialized_model = deserialize_keras_object(deserialized_dict)
print(deserialized_model.summary())
