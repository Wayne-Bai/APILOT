import tensorflow as tf

def create_dtensor_layout(mesh, tensor_shape, layout_spec):
    """
    Represents the layout information of a DTensor.

    Args:
    mesh: A TensorFlow mesh object defining the device topology.
    tensor_shape: A tuple representing the shape of the tensor.
    layout_spec: A string specifying the layout, e.g., 'batch, feature'.

    Returns:
    A DTensor layout object.
    """
    # Parse the layout specification
    layout_components = layout_spec.split(', ')
    
    # Create a dictionary to map layout components to mesh dimensions
    layout_dict = {component: mesh.dim_names[i] for i, component in enumerate(layout_components)}
    
    # Create the layout object
    layout = tf.experimental.dtensor.Layout(layout_dict, mesh)
    
    return layout

# Example usage:
# mesh = tf.experimental.dtensor.create_mesh([('batch', 2), ('feature', 3)])
# tensor_shape = (4, 5)
# layout_spec = 'batch, feature'
# dtensor_layout = create_dtensor_layout(mesh, tensor_shape, layout_spec)
