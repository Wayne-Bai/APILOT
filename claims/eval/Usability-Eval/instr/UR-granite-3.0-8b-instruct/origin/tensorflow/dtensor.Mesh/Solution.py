import tensorflow as tf

class MeshDimensions:
    def __init__(self, name, dimensions):
        self.name = name
        self.dimensions = dimensions

class MeshConfig:
    def __init__(self, mesh_dimensions):
        self.mesh_dimensions = mesh_dimensions

    def __repr__(self):
        return f"MeshConfig(mesh_dimensions={self.mesh_dimensions})"

# Example usage:
mesh_dimensions = MeshDimensions(name="example_mesh", dimensions=[10, 20, 30])
mesh_config = MeshConfig(mesh_dimensions)
print(mesh_config)
