import tensorflow as tf

class AbstractOptimizer(tf.keras.optimizer.Optimizer):
    def __init__(self, **kwargs):
        super(AbstractOptimizer, self).__init__(**kwargs)

    def minimize(self, loss, var_list=None, gate_gradients=tf.compat.v1.GateGradients.ONE_SIDE_NO_OP, aggregation_method=None, colocate_gradients_with_ops=False, name=None):
        raise NotImplementedError("Subclass must implement this method.")

    def get_gradients(self, loss, var_list=None, gate_gradients=tf.compat.v1.GateGradients.ONE_SIDE_NO_OP, aggregation_method=None, colocate_gradients_with_ops=False, name=None):
        raise NotImplementedError("Subclass must implement this method.")
