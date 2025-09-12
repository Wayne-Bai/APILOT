import tensorflow as tf

def find_k_largest(tensor, k):
    return tf.math.top_k(tensor, k=k, sorted=True)
