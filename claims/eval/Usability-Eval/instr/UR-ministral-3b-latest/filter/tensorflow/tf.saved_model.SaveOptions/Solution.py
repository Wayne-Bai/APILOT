import tensorflow as tf

# Define the model (example: a simple neural network)
model = tf.keras.Sequential([
    tf.keras.layers.Dense(64, activation='relu', input_shape=(784,)),
    tf.keras.layers.Dense(10, activation='softmax')
])

# Compile the model
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Save the model to SavedModel format
model.save('my_model')

# Create a new SavedModel function to load the model
my_new_model = tf.keras.models.load_model('my_model')

# Specify the path to load the model from SavedModel format
new_model_path = 'my_model'

# Save the variable directory
new_model_path_variable_dir = new_model_path + '/assets/'
os.mkdir(new_model_path_variable_dir)

# Save the model parameters and variables to the variable directory
my_new_model.save_weights(new_model_path)
