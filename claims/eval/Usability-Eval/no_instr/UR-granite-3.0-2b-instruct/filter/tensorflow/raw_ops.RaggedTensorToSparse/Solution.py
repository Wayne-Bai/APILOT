import tensorflow as tf

def ragged_to_sparse(ragged_tensor):
    # Convert RaggedTensor to SparseTensor
    sparse_tensor = tf. sparse.from_ragged(ragged_tensor, default_value=0)
    return sparse_tensor
