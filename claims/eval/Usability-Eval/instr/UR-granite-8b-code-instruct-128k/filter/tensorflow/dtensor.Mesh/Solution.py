import tensorflow as tf

class Mesh:
    def __init__(self, mesh_dimensions):
        self.mesh_dimensions = mesh_dimensions

    def __repr__(self):
        return f"Mesh configuration over {self.mesh_dimensions} dimensions"