import tensorflow as tf

# Define a sample model
model = tf.keras.Sequential([
    tf.keras.layers.Dense(64, activation='relu', input_shape=(784,)),
    tf.keras.layers.Dense(10, activation='softmax')
])

# Compile the model
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Example data
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()

# Normalize the input
x_train, x_test = x_train / 255.0, x_test / 255.0

# Continues the execution with more feeds and fetches
# Example for training (training mode)
model.fit(x_train, y_train, epochs=5, batch_size=32, validation_data=(x_test, y_test))

# Example for inference (inference mode)
model.summary()
