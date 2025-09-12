
import tensorflow as tf

def top_k(input_tensor, k):
    values, indices = tf.nn.top_k(input_tensor, k=k)
    return values, indices

# Example usage:
input_tensor = tf.constant([[1, 3, 2], [4, 6, 5]])
k = 2
values, indices = top_k(input_tensor, k)
print("Top {} values: {}".format(k, values))
print("Indices of top {} values: {}".format(k, indices))
