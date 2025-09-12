import tensorflow as tf

# Assuming that you have a list of tensors named 'tensor_list' and a list of ids named 'id_list'
# Also, assuming that the weights for each tensor are provided as a list named 'weight_list'

# Create an empty list to store the embeddings
embeddings = []

# Iterate over the list of ids
for id in id_list:
    # Find the corresponding tensor in the tensor_list
    tensor = next((t for t in tensor_list if t.ids[0] == id), None)

    # If the tensor is found, look up the embedding using the weights
    if tensor:
        embedding = tf.nn.embedding_lookup(tensor.weights, id)
        embeddings.append(embedding)

# Convert the list of embeddings to a numpy array
embeddings = np.array(embeddings)
