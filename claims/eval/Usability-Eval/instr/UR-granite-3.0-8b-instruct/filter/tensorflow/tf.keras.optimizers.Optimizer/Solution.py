import tensorflow as tf

class AbstractOptimizer(tf.optimizers.Optimizer):
    def __init__(self, learning_rate, **kwargs):
        super(AbstractOptimizer, self).__init__(learning_rate, **kwargs)

    def minimize(self, loss, var_list=None, gate_gradients=tf.compat.v1.GateOp.GATE_OP_NONE, name=None):
        raise NotImplementedError("This is an abstract class. Please implement the minimize method.")

    def get_updates(self, loss, var_list=None):
        raise NotImplementedError("This is an abstract class. Please implement the get_updates method.")
