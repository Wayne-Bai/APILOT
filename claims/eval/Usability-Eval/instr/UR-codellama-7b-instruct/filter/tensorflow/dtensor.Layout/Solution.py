import tensorflow as tf

class DTensorLayout:
    def __init__(self, shape):
        self.shape = shape

    def get_shape(self):
        return self.shape

    def get_rank(self):
        return len(self.shape)

    def get_num_elements(self):
        num_elements = 1
        for dim in self.shape:
            num_elements *= dim
        return num_elements
