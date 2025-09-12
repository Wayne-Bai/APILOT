
import tensorflow as tf

def lookup_embeddings(ids, tensors_list):
    embeddings = []
    for tensor in tensors_list:
        tensor_shape = tensor.shape.as_list()
        tensor_size = tensor_shape[-1]
        
        if tensor_size is not None:
            emb = tf.gather(tensor, ids)
            embeddings.append(emb)
        else:
            raise ValueError("Tensor dimension must be defined for embedding lookup.")
    
    return embeddings
