import tensorflow as tf

# Building a simple model
model = tf.keras.Sequential([
    tf.keras.layers.Dense(units=128, activation='relu', input_shape=(784,)),
    tf.keras.layers.Dense(units=10, activation='softmax')
])

# Configuring the model for training
# Using 'adam' optimizer, sparse categorical cross-entropy loss, and keeping track of accuracy
model.compile(
    optimizer=tf.keras.optimizers.Adam(),  # Using a modern API call for the Adam optimizer
    loss=tf.keras.losses.SparseCategoricalCrossentropy(),  # Correct modern API for loss
    metrics=['accuracy']  # Specifying metrics to track
)

# The model is now configured for training and can be used with fit() method, e.g.:
# model.fit(x_train, y_train, epochs=10, batch_size=32)
