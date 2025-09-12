import tensorflow as tf

# Create a simple model
model = tf.keras.Sequential([
    tf.keras.layers.Dense(128, activation=tf.nn.relu),
    tf.keras.layers.Dense(1)
])

# Compile the model
model.compile(optimizer='adam', loss='mean_squared_error')

# Fit the model to the data
model.fit(X_train, y_train, epochs=10)

# Save the model to a SavedModel format
model.save('my_model')

# Load the model
loaded_model = tf.keras.models.load_model('my_model')
