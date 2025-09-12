
import tensorflow as tf

# Define the model and its inputs and outputs
model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(64, activation='relu', input_shape=(784,)),
    tf.keras.layers.Dense(10, activation='softmax')
])

# Compile the model with a loss function and an optimizer
model.compile(loss=tf.keras.losses.SparseCategoricalCrossentropy(), optimizer=tf.keras.optimizers.Adam())

# Train the model on some sample data
data = np.random.rand(100, 784)
labels = np.random.randint(0, 2, size=(100,))
model.fit(data, labels, epochs=5)

# Save the model to a SavedModel
tf.saved_model.save(model, 'my_model')
