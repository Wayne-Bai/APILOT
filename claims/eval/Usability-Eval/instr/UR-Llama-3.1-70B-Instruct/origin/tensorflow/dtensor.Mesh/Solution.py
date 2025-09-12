# Import necessary libraries
import tensorflow as tf
from dataclasses import dataclass
from typing import List

# Define data class for Mesh Dimension
@dataclass
class MeshDimension:
    name: str
    size: int

# Define data class for Mesh configuration
@dataclass
class MeshConfiguration:
    dimensions: List[MeshDimension]
    mesh_size: tf.Tensor

    def __post_init__(self):
        # Calculate the mesh size as the product of all dimensions
        self.mesh_size = tf.constant(
            self.dimensions[0].size, dtype=tf.int32
        )
        for dimension in self.dimensions[1:]:
            self.mesh_size *= tf.constant(
                dimension.size, dtype=tf.int32
            )

# Example usage
if __name__ == "__main__":
    # Define mesh dimensions
    mesh_dimensions = [
        MeshDimension("x", 10),
        MeshDimension("y", 20),
        MeshDimension("z", 30),
    ]

    # Create mesh configuration
    mesh_config = MeshConfiguration(mesh_dimensions, None)

    # Print the mesh size
    print("Mesh Size:", mesh_config.mesh_size)
