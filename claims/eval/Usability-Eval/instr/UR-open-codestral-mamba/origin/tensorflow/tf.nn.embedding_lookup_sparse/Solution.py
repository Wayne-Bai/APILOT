import tensorflow as tf

# Assuming you have a list of numpy arrays (tensors) and their corresponding ids and weights
tensor_list = [np.random.rand(10, 2), np.random.rand(10, 3), np.random.rand(10, 4)]
ids_list = [0, 1, 2]
weights_list = [0.5, 0.3, 0.2]

# Convert the list of tensors to a tf.data.Dataset
dataset = tf.data.Dataset.from_tensor_slices((ids_list, weights_list)).batch(1)

# Define a function to lookup embeddings for the given ids and weights
@tf.function
def lookup_embeddings(ids, weights):
    tensor = tensor_list[ids[0]]  # Here we assume that ids[0] always corresponds to the tensor in tensor_list
    embedding = tf.einsum('ij,j->i', tensor, weights)
    return embedding

# Map the function to the dataset
result_dataset = dataset.map(lookup_embeddings)

# Convert the dataset back to a list of numpy arrays
result_list = list(result_dataset)
