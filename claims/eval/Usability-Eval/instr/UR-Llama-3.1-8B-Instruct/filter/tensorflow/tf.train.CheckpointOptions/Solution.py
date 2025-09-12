# Import necessary libraries
import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.callbacks import ModelCheckpoint
from tensorflow.keras.optimizers import Adam

# Define the model architecture
model = models.Sequential([
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(256, 256, 3)),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(128, (3, 3), activation='relu'),
    layers.Flatten(),
    layers.Dense(128, activation='relu'),
    layers.Dense(10)  # Output layer with 10 units (e.g., for 10-class classification)
])

# Compile the model
model.compile(optimizer=Adam(lr=0.001),
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# Define the model checkpoint callback
checkpoint_filepath ='model_checkpoint.ckpt'
model_checkpoint_callback = ModelCheckpoint(
    filepath=checkpoint_filepath,
    save_weights_only=True,
    monitor='val_accuracy',
    mode='max',
    save_best_only=True,
    verbose=1,
    period=1
)

# Define the model save callback (alternative to model checkpoint)
# model_save_callback = ModelCheckpoint(
#     filepath='model_save.h5',
#     save_weights_only=False,
#     monitor='val_accuracy',
#     mode='max',
#     save_best_only=True,
#     verbose=1,
#     period=1
# )

# Train the model
history = model.fit(
    # Replace with your dataset
    None,
    epochs=10,
    batch_size=32,
    validation_split=0.2,
    callbacks=[model_checkpoint_callback]
)

# Load the model from the checkpoint after training is complete
# model.load_weights(checkpoint_filepath)

# Evaluate the model
# loss, accuracy = model.evaluate(
#     # Replace with your dataset
#     None,
#     verbose=2
# )

print("Model Trained and Saved!")
