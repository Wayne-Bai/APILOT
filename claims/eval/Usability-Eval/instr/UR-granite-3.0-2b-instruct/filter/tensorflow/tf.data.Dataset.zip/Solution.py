import tensorflow as tf

# Assuming you have two datasets, dataset1 and dataset2
dataset1 = ...  # define your dataset1
dataset2 = ...  # define your dataset2

# Zip the datasets together
zip_datasets = tf.data.Dataset.from_tensor_slices((dataset1, dataset2))

# Shuffle the zipped dataset
zip_datasets = zip_datasets.shuffle(buffer_size=100)

# Batch the zipped dataset
zip_datasets = zip_datasets.batch(batch_size=32)

# Use the zipped dataset for training or other purposes
for batch in zip_datasets:
    # batch[0] contains the first dataset, batch[1] contains the second dataset
    # process the batches as needed
    pass
