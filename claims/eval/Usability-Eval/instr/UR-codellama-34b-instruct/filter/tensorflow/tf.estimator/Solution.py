import tensorflow as tf
from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split

# Generate a synthetic dataset
X, y = make_regression(n_samples=100, n_features=10)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Create a linear regression model in TensorFlow
model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(1, input_shape=(10,))
])

# Compile the model with the mean squared error loss function and Adam optimizer
model.compile(loss='mse', optimizer='adam')

# Train the model on the training data
model.fit(X_train, y_train, epochs=10)

# Evaluate the model on the testing data
loss = model.evaluate(X_test, y_test)
print('Testing loss:', loss)

# Predict on a new input
new_input = tf.constant([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])
prediction = model.predict(new_input)
print('Predicted output:', prediction)
