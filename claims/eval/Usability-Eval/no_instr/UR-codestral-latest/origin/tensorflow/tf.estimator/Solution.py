import tensorflow as tf
from tensorflow.keras import layers, models

# Create a simple sequential model
def create_model():
    model = models.Sequential()
    model.add(layers.Dense(64, activation='relu', input_shape=(784,)))
    model.add(layers.Dense(64, activation='relu'))
    model.add(layers.Dense(10, activation='softmax'))
    return model

# Compile and train the model
def train_model(model, train_images, train_labels, epochs=5):
    model.compile(optimizer='adam',
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])
    model.fit(train_images, train_labels, epochs=epochs)

# Evaluate the model on test data
def evaluate_model(model, test_images, test_labels):
    test_loss, test_acc = model.evaluate(test_images, test_labels, verbose=2)
    print('\nTest accuracy:', test_acc)

# Use the model to predict a single image
def predict_single_image(model, image):
    prediction = model.predict(image)
    return prediction

# Export the trained model to a saved_model format
def export_model(model, path):
    model.save(path)
