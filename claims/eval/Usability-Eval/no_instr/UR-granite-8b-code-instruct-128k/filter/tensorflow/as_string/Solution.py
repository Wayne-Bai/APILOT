import tensorflow as tf

def convert_tensor_to_strings(tensor):
    return tf.strings.as_string(tensor, precision=0, scientific=False, shortest=False, width=0, fill=' ', zeropad=False)
