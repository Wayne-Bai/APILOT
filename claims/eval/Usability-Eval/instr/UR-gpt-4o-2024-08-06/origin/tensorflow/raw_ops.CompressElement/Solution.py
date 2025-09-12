import tensorflow as tf

# Sample usage of tf.io.encode_proto to compress elements in a dataset
def compress_dataset_element(dataset):
    # Define the compression function using encode_proto
    def compress_element(element):
        # Assuming element is a dictionary of features
        keys, values = zip(*element.items())
        
        # Encoding the values as a serialized proto message
        serialized_proto = tf.io.encode_proto(
            sizes=[len(values)],
            values=values,
            field_names=keys,
            message_type="FeatureMessage"
        )
        
        return serialized_proto

    # Apply the compression function to each element in the dataset
    compressed_dataset = dataset.map(lambda element: compress_element(element))
    
    return compressed_dataset

# Example use case with a simple dataset
sample_features = {
    "feature1": tf.constant([1.0, 2.0]),
    "feature2": tf.constant([3, 4]),
    "feature3": tf.constant(["string1", "string2"])
}

# Create a dataset from the sample features
dataset = tf.data.Dataset.from_tensor_slices(sample_features)

# Compressing elements of the dataset
compressed_dataset = compress_dataset_element(dataset)

# Iterate through and print compressed data examples
for element in compressed_dataset.take(1):
    tf.print("Compressed Element:", element)
