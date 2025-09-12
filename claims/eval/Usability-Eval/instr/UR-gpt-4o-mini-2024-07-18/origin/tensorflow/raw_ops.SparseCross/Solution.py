import tensorflow as tf

def generate_sparse_cross(sparse_tensors, dense_tensors):
    # Ensure all tensors are in the correct format and shape
    sparse_tensors = [tf.convert_to_tensor(st) for st in sparse_tensors]
    dense_tensors = [tf.convert_to_tensor(dt) for dt in dense_tensors]
    
    # Create a list to hold the resulting sparse cross
    sparse_cross_result = []

    # Use tf.sparse to create sparse tensors from the provided inputs
    for sparse in sparse_tensors:
        for dense in dense_tensors:
            # Creating a sparse cross product
            cross_sparse = tf.sparse.sparse_dense_matmul(sparse, tf.expand_dims(dense, axis=0))
            sparse_cross_result.append(cross_sparse)

    # Combine all sparse tensors into a single sparse tensor, if needed
    final_sparse_tensor = tf.sparse.concat(axis=0, sp_inputs=sparse_cross_result)

    return final_sparse_tensor

# Example usage:
sparse_input = [tf.sparse.SparseTensor(indices=[[0, 0], [1, 1]], values=[1, 2], dense_shape=[2, 2])]
dense_input = [tf.constant([[1]], dtype=tf.float32), tf.constant([[2]], dtype=tf.float32)]

result = generate_sparse_cross(sparse_input, dense_input)
print(result)
