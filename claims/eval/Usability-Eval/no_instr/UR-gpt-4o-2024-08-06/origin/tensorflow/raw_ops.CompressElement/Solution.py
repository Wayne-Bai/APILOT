import tensorflow as tf

# Create a simple dataset
dataset = tf.data.Dataset.from_tensor_slices([{"feature1": [1.0, 2.0, 3.0], "feature2": [4.0, 5.0, 6.0]}])

# Function to compress the dataset element
def compress_element(element):
    # Serialize the element
    serialized = tf.io.serialize_tensor(element)
    
    # Compress the serialized tensor
    compressed = tf.io.encode_base64(serialized)
    
    return compressed

# Apply the compression function to each element in the dataset
compressed_dataset = dataset.map(lambda x: compress_element([x['feature1'], x['feature2']]))

# Iterate through the compressed dataset and print each element
for element in compressed_dataset:
    print(element.numpy())
