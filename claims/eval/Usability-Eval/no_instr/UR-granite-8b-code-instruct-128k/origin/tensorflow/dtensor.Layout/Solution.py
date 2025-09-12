import tensorflow as tf

class DTensorLayout:
    def __init__(self, mesh, shape, offset, rank):
        self.mesh = mesh
        self.shape = shape
        self.offset = offset
        self.rank = rank

    def get_tensor_shape(self):
        return self.shape

    def get_tensor_rank(self):
        return self.rank

    def get_tensor_offset(self):
        return self.offset

    def get_tensor_mesh(self):
        return self.mesh
