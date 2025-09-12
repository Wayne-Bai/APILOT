# Import necessary libraries
import tensorflow as tf

class MeshDimension:
    def __init__(self, name, size):
        """
        Represents a dimension of the mesh.

        Args:
        name (str): Name of the dimension.
        size (int): Size of the dimension.
        """
        self.name = name
        self.size = size

class Mesh:
    def __init__(self, dimensions):
        """
        Represents a mesh configuration over a certain list of mesh dimensions.

        Args:
        dimensions (list): List of MeshDimension objects.
        """
        self.dimensions = dimensions

    def get_dimension(self, name):
        """
        Get a dimension by its name.

        Args:
        name (str): Name of the dimension.

        Returns:
        MeshDimension: Dimension with the given name if found, otherwise None.
        """
        for dimension in self.dimensions:
            if dimension.name == name:
                return dimension
        return None

    def add_dimension(self, dimension):
        """
        Add a new dimension to the mesh.

        Args:
        dimension (MeshDimension): Dimension to be added.
        """
        self.dimensions.append(dimension)

    def remove_dimension(self, name):
        """
        Remove a dimension from the mesh by its name.

        Args:
        name (str): Name of the dimension to be removed.
        """
        self.dimensions = [dimension for dimension in self.dimensions if dimension.name!= name]

# Create a mesh with some dimensions
mesh = Mesh([
    MeshDimension('x', 10),
    MeshDimension('y', 20),
    MeshDimension('z', 30)
])

# Get a dimension by its name
print(mesh.get_dimension('y').size)  # Output: 20

# Add a new dimension to the mesh
mesh.add_dimension(MeshDimension('t', 40))
print(mesh.get_dimension('t').size)  # Output: 40

# Remove a dimension from the mesh
mesh.remove_dimension('y')
print(mesh.get_dimension('y'))  # Output: None
