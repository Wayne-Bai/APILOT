import tensorflow as tf
from tensorflow import data

# Define your dataset
dataset = data.Dataset.from_tensor_slices((data.CHILD_AGE, data.GENDER, data.WEIGHT, data.BOOSTED_ACTIVITY))

# Split the dataset into training and evaluation sets
train_size = int(0.8 * len(dataset))
train_dataset = dataset.take(train_size)
eval_dataset = dataset.skip(train_size)

# Define the batch size
BATCH_SIZE = 32

# Prefetch dataset for better performance
train_dataset = train_dataset.batch(BATCH_SIZE).prefetch(buffer_size=tf.data.AUTOTUNE)
eval_dataset = eval_dataset.batch(BATCH_SIZE).prefetch(buffer_size=tf.data.AUTOTUNE)
