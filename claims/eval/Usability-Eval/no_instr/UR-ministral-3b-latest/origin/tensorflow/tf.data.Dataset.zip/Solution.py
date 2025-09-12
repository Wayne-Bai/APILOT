import tensorflow as tf

# Function to zip two datasets
def zip_datasets(dataset1, dataset2):
    def pair(elem1, elem2):
        return elem1, elem2

    return dataset1.map(lambda x, y: pair(x, y))

# Example usage
dataset1 = tf.data.Dataset.from_tensor_slices(([1, 2, 3], [0, 1, 0]))
dataset2 = tf.data.Dataset.from_tensor_slices(([4, 5, 6], [1, 0, 2]))

zipped_dataset = zip_datasets(dataset1, dataset2)

for element in zipped_dataset:
    print(element)
