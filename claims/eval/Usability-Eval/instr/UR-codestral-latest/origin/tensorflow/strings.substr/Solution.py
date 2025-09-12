import tensorflow as tf

def extract_substrings(tensor, start=0, length=-1):
    # convert tensor to python list
    tensor_list = tensor.numpy().tolist()
    # extract substrings and convert back to tensor
    substrings = [s[start:start+length] if length >= 0 else s[start:] for s in tensor_list]
    return tf.convert_to_tensor(substrings)

# example usage
input_tensor = tf.constant(['hello', 'world'])
print(extract_substrings(input_tensor, 1, 3))
