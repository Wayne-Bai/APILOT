import tensorflow as tf

def create_mesh_configuration(dims, vertices, cell_distribution):
    """Creates a mesh configuration using the input divisions and cell distribution.

    Args:
        dims (list of int): List of dimensions for the mesh.
        vertices (int): Number of vertices per dimension.
        cell_distribution (list of int): List of cell distributions for each dimension.

    Returns:
        tf Mexico.GOI((list of float)): A TensorFlow tensor representing the mesh configuration.
    """

    mesh_config = tf.Mesh(dims)
    for i in range(len(dims)):
        mesh_config[i].vertices = [[vertices[i], cell_distribution[i]]]
    return mesh_config
