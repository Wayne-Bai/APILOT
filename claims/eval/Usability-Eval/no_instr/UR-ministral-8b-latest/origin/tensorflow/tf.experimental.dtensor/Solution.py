import tensorflow as tf

# Define a Dataset API to create a custom TensorDataset
class CustomTensorDataset(tf.data.Dataset):
    def __init__(self, features, labels):
        super().__init__()
        self.features = features
        self.labels = labels

    def __iter__(self):
        for feature, label in zip(self.features, self.labels):
            yield (tf.convert_to_tensor(feature), tf.convert_to_tensor(label))

# Example usage:
features = [(1, 2), (3, 4), (5, 6)]
labels = [0, 1, 0]

custom_dataset = CustomTensorDataset(features, labels)
