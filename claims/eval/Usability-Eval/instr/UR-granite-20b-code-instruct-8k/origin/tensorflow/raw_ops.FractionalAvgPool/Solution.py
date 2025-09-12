
import tensorflow as tf

inputs = tf.keras.Input(shape=(224, 224, 3))
outputs = tf.keras.layers.FractionalAvgPool2D(pool_size=(2, 2), strides=(2, 2), padding='same')(inputs)
model = tf.keras.Model(inputs=inputs, outputs=outputs)

