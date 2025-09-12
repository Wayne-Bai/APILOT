import tensorflow as tf

def sparse_cross(input_sparse, input_dense):
    input_sparse_dense = tf.nn.sparse_softmax_cross_entropy_with_logits(
        labels=input_sparse,
        logits=input_dense
    )

    return input_sparse_dense
