
import tensorflow as tf

# Define the model and its inputs and outputs
model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(64, activation='relu', input_shape=(784,)),
    tf.keras.layers.Dense(10, activation='softmax')
])

# Compile the model with a loss function and an optimizer
model.compile(loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              optimizer=tf.keras.optimizers.Adam(lr=0.001))

# Define the serialized protobuf binary string representation of the model
model_str = model.to_protobuf()
