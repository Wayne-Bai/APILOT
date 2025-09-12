
import tensorflow as tf

def lookup_embeddings(ids, weights, tensors):
    embeddings = []
    for i in range(len(ids)):
        lookup_id = ids[i]
        lookup_weight = weights[i]
        tensor_idx = int(lookup_id / len(tensors))
        tensor_offset = lookup_id % len(tensors)
        embed = tf.gather(tensors[tensor_idx], tensor_offset)
        embeddings.append(embed * lookup_weight)
    return embeddings

# Test the function
ids = [3, 0, 6]
weights = [0.5, 0.3, 0.2]
tensors = [tf.Variable([[3.1, 2.3], [1.3, 4.1]]), tf.Variable([[5.5], [2.2], [3.3]])]

result = lookup_embeddings(ids, weights, tensors)
print(result)
