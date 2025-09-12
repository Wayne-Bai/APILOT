# Import necessary libraries
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

# Load the example TFModel from SavedModel
model = tf.keras.applications.VGG16(weights='imagenet', include_top=None)

# Freeze the layers
for layer in model.layers:
    layer.trainable = False

# Warm up the model to avoid any model running errors
input_ = tf.random.normal((1, 224, 224, 3))
output = model(input_, training=False)

# Serialize and sign the model
model_signer = tf.saved_model.SignatureSaver(
    input_type_signature=layers.InputSpec(
        shape=(1, 224, 224, 3),
        dtype=tf.float32
    ),
    output_type_signature=layers.OutputSpec(
        shape=(7, 7, 512),
        dtype=tf.float32
    )
)

# Compile the model
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Save the model with the signature
path_to_saved_model = "my_model"
tf.saved_model.save(
    model,
    path_to_saved_model,
    signatures=model_signer.signatures["serving_default"]
)


# Load the model and serialize it
loaded_model = tf.saved_model.load(path_to_saved_model)
loaded_signatures = loaded_model.signatures["serving_default"]

# Get the serialized Protobuf binary string representation
serialized_model_bytes = loaded_signatures.serialize_to_buffer()

print(serialized_model_bytes)
