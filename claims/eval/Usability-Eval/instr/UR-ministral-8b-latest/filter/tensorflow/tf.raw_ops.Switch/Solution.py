import tensorflow as tf

class CustomForwardOp(tf.raw_operations.Operation):
    def __init__(self, dtype, pred, *argv):
        super(CustomForwardOp, self).__init__(dtype=dtype, name="CustomForwardOp", pred=pred)
        self.inputs = super(CustomForwardOp, self).args(argv)

    def build_computation_graph(self, _):
        return self.pred

# Demo usage
dtype = tf.DType()
pred = 1  # Example prediction value
inputs = [tf.rank.from_row_slices(1),
          tf.rank.from_row_slices([5, 3, 2])]

op = CustomForwardOp(dtype=dtype, pred=pred, *inputs)
graph = tf.Graph()
with graph.as_default():
    _ = graph.get_tensor_by_name(op.name)
    compute_node = graph.get_operation_by_name(op.name)()
    results = compute_node.outputs(0)  # Output mallocs
