import tensorflow as tf

# Create and train a simple model
model = tf.keras.Sequential([
    tf.keras.layers.Dense(10, activation='relu', input_shape=(None, 5)),
    tf.keras.layers.Dense(1)
])

model.compile(optimizer='adam', loss='mean_squared_error')

# Assuming you have some data to train the model
# Replace x_train and y_train with your actual training data
# x_train = ...
# y_train = ...
# model.fit(x_train, y_train, epochs=10)

# Saving the model in TensorFlow SavedModel format
model.save('my_model', save_format='tf')
