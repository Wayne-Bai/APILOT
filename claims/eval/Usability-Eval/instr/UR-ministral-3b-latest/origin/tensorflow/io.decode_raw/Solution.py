from tensorflow.keras import backend as K
import tensorflow as tf

def raw_bytes_to_numeric(raw_byte_tensor):
    # Convert bytes tensor to numpy array
    input_tensors_data = K.eval(raw_byte_tensor)

    # Assuming the input data is already bytes and the size is consistent
    numeric_tensor = tf.convert_to_tensor(input_tensors_data, dtype=tf.uint8)

    # Convert the Tensor to a Numpy array
    numeric_array = numeric_tensor.numpy()

    return numeric_array
