
import tensorflow as tf

# Assuming you have a tensor of strings called 'input_tensor'
# and you want to extract substrings from it.

# Define the start and end indices of the substrings you want to extract
start_index = 0
end_index = 2

# Extract the substrings using tensorflow string slice operation
output_tensor = input_tensor[:, start_index:end_index]

# Print the substrings
print(output_tensor.numpy())
