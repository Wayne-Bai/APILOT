import tensorflow as tf
from tensorflow.keras import models, layers
from tensorflow.keras.applications import VGG16

def image_classification_model():
    model = models.Sequential()
    model.add(layers.Conv2D(32, (3,3), activation='relu', input_shape=(256, 256, 3)))
    model.add(layers.MaxPooling2D((2, 2)))
    model.add(layers.Flatten())
    model.add(layers.Dense(units=64, activation='relu'))
    model.add(layers.Dense(units=10, activation='softmax'))
    return model

def store_model_to_protobuf(model):
    model.save('model.h5')
    with tf.io.gfile.GFile('model.h5', 'rb') as f:
        model_data = f.read()
    with tf.io.gfile.GFile('model.pb', 'wb') as f:
        f.write(tf.compat.v1.protobuf.MessageLite.SerializeToString(model_data))
    print("Model successfully saved to model.pb")

# Create model
model = image_classification_model()

# Store the model to protobuf
store_model_to_protobuf(model)
