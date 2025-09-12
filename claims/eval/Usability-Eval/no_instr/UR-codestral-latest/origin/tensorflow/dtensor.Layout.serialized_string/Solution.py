import tensorflow as tf
from tensorflow.io import serialize_tensor

def serialize_tf_tensor(tensor):
    # serialize the tensor
    serialized_tensor = serialize_tensor(tensor)

    return serialized_tensor
