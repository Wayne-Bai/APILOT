import tensorflow as tf

class CustomMesh:
    def __init__(self, mesh_dims):
        """
        Initialize a Mesh configuration based on provided mesh dimensions.

        Args:
        mesh_dims (list of tuples): List where each tuple consists of a name and the size of that dimension.
        """
        self.mesh_dims = mesh_dims

    def create_devices(self):
        """
        Create a list of virtual devices (logical CPUs) based on the mesh dimensions.
        """
        devices = []
        for dim_name, dim_size in self.mesh_dims:
            devices.extend([f'{dim_name}:{i}' for i in range(dim_size)])
        return devices

    def mesh_details(self):
        """
        Print out the details of the mesh configuration.
        """
        for dim_name, dim_size in self.mesh_dims:
            print(f'Dimension {dim_name} with size {dim_size}')

# Usage
mesh_dims = [('X', 2), ('Y', 3)]
mesh = CustomMesh(mesh_dims)

# Print mesh details
mesh.mesh_details()

# Get virtual devices for the configured mesh
devices = mesh.create_devices()
print("Virtual devices created:", devices)
