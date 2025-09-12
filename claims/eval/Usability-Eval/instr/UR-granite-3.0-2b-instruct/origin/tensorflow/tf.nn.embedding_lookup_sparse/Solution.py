import tensorflow as tf

# Assuming that you have a list of tensors named 'tensor_list'
# and a list of ids named 'id_list'

# Look up embeddings for the given ids and weights from a list of tensors
embedded_ids = [tf.nn.embedding_lookup(tensor, id) for tensor, id in zip(tensor_list, id_list)]
