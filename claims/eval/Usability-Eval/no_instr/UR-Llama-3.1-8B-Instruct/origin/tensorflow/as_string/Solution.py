# Import the necessary libraries
import tensorflow as tf

def convert_to_strings(tensor):
    """
    Converts each entry in the given tensor to strings.
    
    Args:
    tensor: A tensorflow tensor.
    
    Returns:
    A tensorflow tensor where each entry is converted to a string.
    """
    
    # Convert the tensor to an array
    array = tensor.numpy()
    
    # Initialize an empty list to store the strings
    strings = []
    
    # Loop over each entry in the array
    for entry in array:
        # Convert the entry to a string and add it to the list
        strings.append(str(entry))
    
    # Create a tensor from the list of strings
    string_tensor = tf.constant(strings)
    
    return string_tensor

# Create a sample tensor
tensor = tf.constant([1, 2, 3, 4, 5])

# Call the function to convert the tensor to strings
string_tensor = convert_to_strings(tensor)

print(string_tensor)
