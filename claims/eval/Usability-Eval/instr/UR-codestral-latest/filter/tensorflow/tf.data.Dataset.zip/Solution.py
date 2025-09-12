import tensorflow as tf

def zip_datasets(dataset1, dataset2):
    zipped_dataset = tf.data.Dataset.zip((dataset1, dataset2))
    return zipped_dataset
