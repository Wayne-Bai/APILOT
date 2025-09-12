import tensorflow as tf

class MeshConfiguration:
    def __init__(self, mesh_dimensions):
        self.mesh_dimensions = mesh_dimensions
        self.mesh = self.create_mesh()

    def create_mesh(self):
        # Create a mesh grid based on the specified dimensions
        return tf.meshgrid(*[tf.range(dim) for dim in self.mesh_dimensions], indexing='ij')

    def get_mesh(self):
        # Return the mesh as a list of tensors
        return [tf.convert_to_tensor(grid) for grid in self.mesh]

# Example usage
if __name__ == "__main__":
    dimensions = [4, 3]  # Example dimensions
    mesh_config = MeshConfiguration(dimensions)
    mesh = mesh_config.get_mesh()

    for i, grid in enumerate(mesh):
        print(f"Mesh grid {i}:")
        print(grid.numpy())
