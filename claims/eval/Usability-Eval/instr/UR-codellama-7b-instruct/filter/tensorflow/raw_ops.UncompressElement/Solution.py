
import tensorflow as tf
from tensorflow import raw_ops

def uncompress(data):
    # Define the input tensor shape and dtype
    input_shape = data.get_shape()
    input_dtype = data.dtype

    # Convert the input to a numpy array
    np_data = data.numpy()

    # Uncompress the data using the uncompress method in raw_ops
    output = raw_ops.uncompress(np_data)

    # Create a new tensor with the uncompressed data
    uncompressed = tf.convert_to_tensor(output, shape=input_shape, dtype=input_dtype)

    return uncompressed
