import tensorflow as tf

# Let's create a simple model
model = tf.keras.Sequential([
    tf.keras.layers.Dense(128, activation='relu', input_shape=(784,)),
    tf.keras.layers.Dense(10, activation='softmax')
])

# Compile the model with an optimizer, loss function and metric
model.compile(
    optimizer='adam',  # Using Adam optimizer
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

# Assuming we have training data loaded in X_train and y_train
# For example purposes, let's create some dummy data
import numpy as np 

X_train = np.random.random((1000, 784))
y_train = np.random.randint(10, size=(1000,))

# Train the model
model.fit(X_train, y_train, epochs=10)
