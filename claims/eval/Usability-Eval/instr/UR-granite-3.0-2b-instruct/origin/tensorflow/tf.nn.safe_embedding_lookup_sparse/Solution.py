import tensorflow as tf

# Define the embedding layer
embedding_layer = tf.keras.layers.Embedding(input_dim=10000, output_dim=64, input_length=10)

# Define the model
model = tf.keras.Sequential([
    embedding_layer,
    tf.keras.layers.LSTM(units=64, return_sequences=True),
    tf.keras.layers.LSTM(units=64),
    tf.keras.layers.Dense(units=10, activation='softmax')
])

# Compile the model
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Prepare the data
# Assuming you have a dataset with features and labels
# features = ...
# labels = ...

# Add padding to the features
padded_features = tf.keras.preprocessing.sequence.pad_sequences(features, maxlen=10, padding='post')

# Create a mask to handle invalid IDs
mask = tf.math.not_equal(padded_features, 0)

# Create a masked version of the padded features
masked_features = tf.boolean_mask(padded_features, mask)

# Create a mask for the labels
label_mask = tf.math.not_equal(labels, -1)

# Create a masked version of the labels
masked_labels = tf.boolean_mask(labels, label_mask)

# Train the model
model.fit(masked_features, masked_labels, epochs=10, batch_size=32)
