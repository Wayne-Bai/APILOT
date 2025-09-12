import tensorflow as tf

def substrings_from_tensor(input_tensor, start_indices, num_values):
    """
    Returns substrings from a tensor of strings.
    
    Args:
    input_tensor (tf.Tensor): The input tensor of strings.
    start_indices (tf.Tensor): The start indices for the substrings.
    num_values (int): The number of substrings to return.
    
    Returns:
    tf.Tensor: A tensor of substrings.
    """
    
    # Convert the input tensor to a RaggedTensor
    input_ragged = tf.strings.unicode_decode(input_tensor, 'UTF-8')
    
    # Calculate the end indices
    end_indices = start_indices + num_values
    
    # Create a boolean mask to select the substring characters
    mask = tf.sequence_mask(end_indices - start_indices, maxlen=tf.reduce_max(end_indices))
    
    # Create the substring RaggedTensor
    substrings_ragged = tf.ragged.boolean_mask(input_ragged, mask)
    
    # Crop the substrings RaggedTensor to the specified bounds
    substrings_cropped = tf.strings.unicode_encode(substrings_ragged[:, start_indices: end_indices], 'UTF-8')
    
    return substrings_cropped

# Test the function
input_tensor = tf.constant(['hello world', 'example text'])
start_indices = tf.constant([6, 9])
num_values = 5

result = substrings_from_tensor(input_tensor, start_indices, num_values)

print(result)
