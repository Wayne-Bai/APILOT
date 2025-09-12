import tensorflow as tf

# Define a simple linear regression model
model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(units=1, input_shape=(1,))
])

# Compile the model with a mean squared error loss function and an Adam optimizer
model.compile(loss='mse', optimizer='adam')

# Generate some sample data for training
x_train = np.random.randn(100, 1)
y_train = np.random.randn(100)

# Train the model on the sample data
model.fit(x_train, y_train, epochs=100, batch_size=32)

# Evaluate the model on a test set
test_loss = model.evaluate(np.random.randn(50, 1), np.random.randn(50))
print('Test loss:', test_loss)

# Predict output for some input data using the trained model
predictions = model.predict(np.random.randn(50, 1))
print('Predicted values:', predictions)

# Export the model as a SavedModel
tf.saved_model.save(model, 'my_model')
