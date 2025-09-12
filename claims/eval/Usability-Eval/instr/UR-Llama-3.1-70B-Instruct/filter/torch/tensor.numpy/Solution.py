# Importing the torch library
import torch

# Create a tensor
tensor = torch.tensor([1, 2, 3])

# Function to convert tensor to numpy array
def convert_to_numpy(tensor):
    return tensor.detach().cpu().numpy()

# Convert tensor to numpy array
numpy_array = convert_to_numpy(tensor)

# Print the results
print("Tensor: ", tensor)
print("Numpy Array: ", numpy_array)

# Verify the type
print("Type of Tensor: ", type(tensor))
print("Type of Numpy Array: ", type(numpy_array))
