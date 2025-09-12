import tensorflow as tf

datasets = [tf.data.Dataset.from_tensor_slices(tf.random.normal([10, 5])),
            tf.data.Dataset.from_tensor_slices(tf.random.normal([20, 5]))]

zipped_dataset = tf.data.Dataset.zip(datasets)

for element in zipped_dataset:
    print(element)
