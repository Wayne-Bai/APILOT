import tensorflow as tf
from tensorflow.keras.utils import to_categorical

# Assuming you have a dataset with features X and labels y
# X = ...
# y = ...

# Convert labels to categorical format
y = to_categorical(y)

# Define a TensorFlow dataset from your features and labels
dataset = tf.data.Dataset.from_tensor_slices((X, y))

# Shuffle the dataset
dataset = dataset.shuffle(buffer_size=1024)

# Batch the dataset
dataset = dataset.batch(batch_size=32)

# Create a TensorFlow dataset iterator
iterator = dataset.iter

# Iterate over the dataset
for batch in iterator:
    # Access the features and labels from the batch
    X_batch, y_batch = batch

    # Your code to process the batch goes here
    # ...
