# Importing necessary libraries
import tensorflow as tf

# Define a simple model
model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(512, activation='relu', input_shape=(784,)),
    tf.keras.layers.Dense(10, activation='softmax')
])

# Define a data generator
def data_generator():
    for _ in range(100):
        yield tf.random.normal([1, 784])

# Using ProtobufEncoder to serialize the model
serialize_model = tf.keras.models.serialize_keras_model(model)
serialize_proto = serialize_model.to_proto()
serialized_model = serialize_proto.SerializeToString()

print(serialized_model)
