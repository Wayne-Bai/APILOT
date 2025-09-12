import numpy as np
import tensorflow as tf

# Generate some random data
np.random.seed(0)
n_samples = 200
X = np.random.randn(n_samples, 20)
y = np.random.randn(n_samples)

# Define the TensorFlow platform to perform PLS regression
pls_model = tf.keras.Sequential([
    tf.keras.layers.Dense(20, activation='relu', input_dim=20),
    tf.keras.layers.Dense(1, activation='linear')  # For one output
])

pls_model.compile(loss='mean_squared_error', optimizer='adam')

# Fit data to model
pls_model.fit(X, y, epochs=10, verbose=1)

# Predict on the same data
y_pred = pls_model.predict(X)
