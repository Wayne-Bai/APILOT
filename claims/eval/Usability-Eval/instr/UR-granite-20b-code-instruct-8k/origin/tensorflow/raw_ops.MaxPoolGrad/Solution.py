import tensorflow as tf

# Define the input tensor
input = tf.keras.Input(shape=(28, 28, 1))

# Define the model
x = tf.keras.layers.Conv2D(32, (3, 3), activation='relu')(input)
x = tf.keras.layers.MaxPooling2D(2, 2)(x)
x = tf.keras.layers.Flatten()(x)
output = tf.keras.layers.Dense(10, activation='softmax')(x)

# Create the model
model = tf.keras.Model(inputs=input, outputs=output)

# Compile the model
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
