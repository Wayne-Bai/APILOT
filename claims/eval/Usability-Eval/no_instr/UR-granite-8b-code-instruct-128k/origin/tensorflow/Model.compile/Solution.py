import tensorflow as tf
# Define the model architecture
model = tf.keras.models.Sequential([
 tf.keras.layers.Flatten(),
 tf.keras.layers.Dense(128, activation='relu'),
 tf.keras.layers.Dropout(0.2),
 tf.keras.layers.Dense(10, activation='softmax')
])
# Compile the model
model.compile(
 optimizer='adam',
 loss='sparse_categorical_crossentropy',
 metrics=['accuracy']
)
# Configure the model for training
model.fit(
 train_images,
 train_labels,
 epochs=10,
 validation_data=(test_images, test_labels)
)
