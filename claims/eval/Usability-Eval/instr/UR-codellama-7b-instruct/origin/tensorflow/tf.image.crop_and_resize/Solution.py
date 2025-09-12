
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

def extract_crops(image, crop_size):
    # define the model architecture
    inputs = keras.Input(shape=(28, 28))
    x = layers.Conv2D(32, (3, 3), activation='relu')(inputs)
    x = layers.MaxPooling2D((2, 2))(x)
    x = layers.Flatten()(x)
    outputs = layers.Dense(10, activation='softmax')(x)

    # compile the model
    model = keras.Model(inputs=inputs, outputs=outputs)
    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

    # create a tensor to hold the crops
    crops = tf.zeros((0, crop_size, crop_size, 3))

    # loop through each image in the batch
    for i in range(image.shape[0]):
        # extract a crop from the current image
        crop = tf.image.extract_patches(
            images=[image[i]],
            sizes=[1, crop_size, crop_size, 1],
            strides=[1, 1, 1, 1],
            rates=[1, 1, 1, 1],
            padding='SAME'
        )

        # add the crop to the tensor of crops
        crops = tf.concat([crops, crop], axis=0)

    return crops
