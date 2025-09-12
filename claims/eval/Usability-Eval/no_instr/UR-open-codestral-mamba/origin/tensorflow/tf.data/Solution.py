import tensorflow as tf
import tensorflow_datasets as tfds

# Import the dataset
dataset, dataset_info = tfds.load('mnist', with_info=True, as_supervised=True)

# Divide the dataset into train and test subsets
train_data, test_data = dataset['train'], dataset['test']

# For instance, to generate one batch of train samples:
train_samples = train_data.batch(32)
