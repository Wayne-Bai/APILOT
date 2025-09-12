import tensorflow as tf

dataset = tf.data.Dataset.from_tensor_slices((input_data, labels))  # assuming inputs and labels are tensors or numpy arrays
dataset = dataset.batch(batch_size)  # batch your data, 'batch_size' is the number of samples in one batch
dataset = dataset.prefetch(buffer_size=tf.data.experimental.AUTOTUNE)  # improves the speed of data loading, reduces latency
dataset = dataset.repeat(num_epochs)  # to repeat the process for 'num_epochs' times
shuffled_dataset = dataset.shuffle(buffer_size=buffer_size)  # optional, replaces the 'shuffle' API
