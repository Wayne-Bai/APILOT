import tensorflow as tf
from tensorflow.keras.optimizers import Adam

# Define a simple model
model = tf.keras.Sequential([
    tf.keras.layers.Dense(64, activation='relu', input_shape=(32,)),
    tf.keras.layers.Dense(1, activation='sigmoid')
])

# Compile the model with Adam optimizer
model.compile(optimizer=Adam(learning_rate=0.001),
              loss='binary_crossentropy',
              metrics=['accuracy'])

# Print the model summary
model.summary()

# Example to show how to train the model
def train_model(data, labels):
    # Assuming 'data' is your input data and 'labels' are the corresponding labels
    model.fit(data, labels, epochs=10, batch_size=32)

# Example to demonstrate how to make predictions
def make_prediction(new_data):
    prediction = model.predict(new_data)
    return prediction

# Note: `data`, `labels`, and `new_data` should be replaced with actual dataset and new data for prediction respectively.
