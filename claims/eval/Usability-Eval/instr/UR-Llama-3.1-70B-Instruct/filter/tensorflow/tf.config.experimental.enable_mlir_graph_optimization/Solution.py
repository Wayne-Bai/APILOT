import tensorflow as tf

# Check TensorFlow version
print("TensorFlow version: ", tf.__version__)

# Enable MLIR-Based TensorFlow Compiler Optimizations
tf.config.experimental.enable_mlir_bridge()

# Create a simple model for testing
model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(64, activation='relu', input_shape=(784,)),
    tf.keras.layers.Dense(32, activation='relu'),
    tf.keras.layers.Dense(10)
])

# Compile the model
model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])

# Test the model
ashion_mnist = tf.keras.datasets.fashion_mnist
(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()
train_images, test_images = train_images / 255.0, test_images / 255.0

# Reshape input data
train_images = train_images.reshape((60000, 784))
test_images = test_images.reshape((10000, 784))

# Evaluate the model
test_loss, test_acc = model.evaluate(test_images,  test_labels, verbose=2)
print('\nTest accuracy:', test_acc)
