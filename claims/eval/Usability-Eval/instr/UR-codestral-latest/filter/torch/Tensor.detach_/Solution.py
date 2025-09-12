import torch

# Assuming we have a tensor 'input_tensor'
# To detach the tensor from the graph that created it
detached_tensor = input_tensor.detach()
# Now 'detached_tensor' is a leaf tensor
