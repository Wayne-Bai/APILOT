
import tensorflow as tf

class DTensorLayout:
    def __init__(self, ndims, dims):
        self.ndims = ndims
        self.dims = dims
    
    def print_layout(self):
        print("Number of dimensions:", self.ndims)
        print("Dimensions:", self.dims)

# Example Usage
layout_info = DTensorLayout(ndims=3, dims=[32, 32, 64])
layout_info.print_layout()
