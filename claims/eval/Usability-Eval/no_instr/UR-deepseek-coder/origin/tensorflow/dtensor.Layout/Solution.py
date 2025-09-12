import tensorflow as tf

class DTensorLayout:
    def __init__(self, mesh, layout):
        self.mesh = mesh
        self.layout = layout

    def get_layout(self):
        return self.layout

    def get_mesh(self):
        return self.mesh

# Example usage:
# mesh = tf.experimental.dtensor.Mesh([1, 2], [('x', 2)], tf.experimental.dtensor.create_device_list([('GPU:0', 'GPU:1')], 'GPU'))
# layout = tf.experimental.dtensor.Layout([tf.experimental.dtensor.UNSHARDED, 'x'], mesh)
# dtensor_layout = DTensorLayout(mesh, layout)
