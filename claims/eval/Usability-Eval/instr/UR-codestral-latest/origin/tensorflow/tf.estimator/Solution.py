import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

# Create a simple sequential model
def create_model():
    model = keras.Sequential([
        layers.Dense(512, activation='relu', input_shape=(784,)),
        layers.Dropout(0.2),
        layers.Dense(10)
    ])

    model.compile(optimizer='adam',
                  loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
                  metrics=['accuracy'])

    return model

# Create a basic model instance
model = create_model()

# Display the model's architecture
model.summary()

# Assume we have some data
# (x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()
# Normalize data values to the range [0, 1].
# x_train = x_train / 255.0
# x_test = x_test / 255.0

# Train the model for a few epochs
# model.fit(x_train, y_train, epochs=5)

# Evaluate the model on the test data using `evaluate`
# print("Evaluate on test data")
# results = model.evaluate(x_test, y_test, batch_size=128)
# print("test loss, test acc:", results)

# Predict on new data
# predictions = model.predict(x_test[:3])

# Save the entire model to a HDF5 file.
# The '.h5' extension indicates that the model should be saved to HDF5.
# model.save('my_model.h5')
