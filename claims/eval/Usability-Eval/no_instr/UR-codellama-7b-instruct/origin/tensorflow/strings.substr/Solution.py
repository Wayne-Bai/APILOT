
import tensorflow as tf

def get_substrings(input_tensor, window_size):
    # Compute the number of substrings we want to extract
    num_substrings = input_tensor.shape[0] - window_size + 1
    
    # Initialize an empty tensor to store the substrings
    output_tensor = tf.zeros(shape=(num_substrings, window_size))
    
    # Iterate over each substring in the input tensor
    for i in range(num_substrings):
        # Get the starting index of the substring
        start_index = i
        
        # Get the ending index of the substring
        end_index = start_index + window_size
        
        # Extract the substring from the input tensor
        substring = input_tensor[start_index:end_index]
        
        # Add the substring to the output tensor
        output_tensor[i] = substring
    
    return output_tensor
