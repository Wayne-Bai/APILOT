import tensorflow as tf
import numpy as np

# Let's create some sample datasets
dataset1 = tf.data.Dataset.range(10).repeat()
dataset2 = tf.data.Dataset.range(10).repeat()

print(f"Dataset 1: {dataset1}")
print(f"Dataset 2: {dataset2}")


def create_dataset_zip(dataset1, dataset2):
    """
    Create a dataset by zipping together two given datasets.

    Args:
        dataset1 (tf.data.Dataset): The first dataset.
        dataset2 (tf.data.Dataset): The second dataset.

    Returns:
        tf.data.Dataset: A new dataset that zips together dataset1 and dataset2.
    """

    # Zip the two datasets together
    zipped_dataset = tf.data.Dataset.zip((dataset1, dataset2))

    return zipped_dataset


zipped_dataset = create_dataset_zip(dataset1, dataset2)
print("Zipped Dataset:")
print(zipped_dataset)
