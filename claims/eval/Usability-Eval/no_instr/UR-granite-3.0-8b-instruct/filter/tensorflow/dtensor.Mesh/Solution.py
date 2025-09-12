import tensorflow as tf

class MeshDimensions:
    def __init__(self, dimensions):
        self.dimensions = dimensions

    def __repr__(self):
        return f"MeshDimensions({self.dimensions})"

class MeshConfig:
    def __init__(self, mesh_dimensions):
        self.mesh_dimensions = mesh_dimensions

    def __repr__(self):
        return f"MeshConfig({self.mesh_dimensions})"

# Example usage:
mesh_dimensions = MeshDimensions([2, 3, 4])
mesh_config = MeshConfig(mesh_dimensions)
print(mesh_config)
