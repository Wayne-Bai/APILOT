import tensorflow as tf

def fill_empty_rows(input_tensor, default_value):
    # Convert the input SparseTensor to a dense tensor
    dense_tensor = tf.sparse.to_dense(input_tensor)

    # Fill empty rows with the default value
    filled_tensor = tf.sparse.from_dense(dense_tensor, default_value)

    return filled_tensor
