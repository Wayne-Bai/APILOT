import tensorflow as tf

# Define a model for convolution
model = tf.keras.Sequential([
    tf.keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
    tf.keras.layers.MaxPooling2D((2, 2)),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(10, activation='softmax')
])

# Create some dummy data for the example
input_data = tf.random.normal([10, 28, 28, 1])
labels = tf.random.normal([10, 10])

# Compute the model's output
output_data = model(input_data)

# Define a loss function
loss_fn = tf.keras.losses.SparseCategoricalCrossentropy()

# Compute the loss
loss = loss_fn(labels, output_data)

# Compute the gradients of the loss with respect to the input
grads = tf.gradients(loss, input_data)

# Print the gradients
for grad in grads:
    print(grad)
