import tensorflow as tf

class DTensorLayout:
    def __init__(self, shape, strides, data_type):
        self.shape = shape
        self.strides = strides
        self.data_type = data_type

    def __repr__(self):
        return f"DTensorLayout({self.shape}, {self.strides}, {self.data_type})"

# Example usage:
dt_layout = DTensorLayout(shape=[2, 3], strides=[6, 1], data_type="float32")
print(dt_layout)
