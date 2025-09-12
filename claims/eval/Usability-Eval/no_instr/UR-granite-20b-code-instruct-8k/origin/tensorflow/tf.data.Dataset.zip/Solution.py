import tensorflow as tf

datasets = [tf.data.Dataset.from_tensor_slices([1, 2, 3]), 
            tf.data.Dataset.from_tensor_slices([4, 5, 6])]

zipped_dataset = tf.data.Dataset.zip(datasets)

for element in zipped_dataset:
    print(element)
