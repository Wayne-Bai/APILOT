import tensorflow as tf

# Define a simple Sequential model
model = tf.keras.Sequential([
    tf.keras.layers.Dense(512, activation='relu', input_shape=(784,)),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(10, activation='softmax')
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Dummy data for illustration purposes
# Normally, you would use a real dataset
import numpy as np
train_data = np.random.random((1000, 784))
train_labels = np.random.randint(10, size=(1000,))

# Train the model
model.fit(train_data, train_labels, epochs=5)

# Save the entire model as a SavedModel
model.save('saved_model/my_model')
