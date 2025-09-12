import tensorflow as tf

def tensor_to_strings(tensor):
    # Convert tensor to numpy array
    numpy_array = tensor.numpy()
    
    # Convert each element in the numpy array to string
    string_array = [str(element) for element in numpy_array]
    
    # Convert the list of strings back to a tensor
    string_tensor = tf.convert_to_tensor(string_array, dtype=tf.string)
    
    return string_tensor

# Example usage:
tensor = tf.constant([1.0, 2.0, 3.0])
result = tensor_to_strings(tensor)
print(result)
