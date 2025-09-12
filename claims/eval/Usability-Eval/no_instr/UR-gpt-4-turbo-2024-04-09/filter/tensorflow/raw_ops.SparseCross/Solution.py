import tensorflow as tf

def sparse_cross_example(sparse_tensors, dense_tensors):
    # Convert dense tensors to sparse tensors
    converted_sparse_tensors = [tf.sparse.from_dense(t) for t in dense_tensors]
    
    # Combine all tensors to form a list for sparse cross operation
    all_tensors = sparse_tensors + converted_sparse_tensors
    
    # Use `tf.sparse.cross` which replaces the outdated `tf.raw_ops.SparseCross`
    sparse_crossed_tensors = tf.sparse.cross(all_tensors)

    return sparse_crossed_tensors

# Example usage
if __name__ == "__main__":
    # Create dummy sparse tensors
    st1 = tf.SparseTensor(indices=[[0,0], [1,2]], values=[1,2], dense_shape=[3,4])
    st2 = tf.SparseTensor(indices=[[0,1], [1,3]], values=[3,4], dense_shape=[3,4])
    
    # Create dummy dense tensors
    dt1 = tf.constant([1, 2, 3])
    dt2 = tf.constant([4, 5, 6])
    
    result = sparse_cross_example([st1, st2], [dt1, dt2])
    print(result)
