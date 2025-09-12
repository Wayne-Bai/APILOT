import tensorflow as tf

# Define a simple Sequential model
model = tf.keras.Sequential([
    tf.keras.layers.Dense(10, activation='relu', input_shape=(None, 5)),
    tf.keras.layers.Dense(10, activation='relu'),
    tf.keras.layers.Dense(1)
])

# Compile the model
model.compile(optimizer='adam',
              loss='mse',
              metrics=['mean_squared_error'])

# Assume some training data (X_train, y_train), validation data (X_val, y_val)
# Just for example purposes, using random numbers instead of real dataset
import numpy as np
X_train = np.random.random((100, 5))
y_train = np.random.random((100, 1))
X_val = np.random.random((20, 5))
y_val = np.random.random((20, 1))

# Train the model
model.fit(X_train, y_train, epochs=10, validation_data=(X_val, y_val))

# Evaluate the model
loss, mse = model.evaluate(X_val, y_val, verbose=2)

# Predict with the model
predictions = model.predict(X_val)

# Save the model
model.save('saved_model/my_model')

# Export the model for TensorFlow Serving
tf.saved_model.save(model, 'exported_model/')
