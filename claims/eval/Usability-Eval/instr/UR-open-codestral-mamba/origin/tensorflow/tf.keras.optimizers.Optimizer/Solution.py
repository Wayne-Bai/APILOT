import tensorflow as tf

class AbstractOptimizer(tf.keras.optimizers.Optimizer):
    def __init__(self, learning_rate, name='AbstractOptimizer', **kwargs):
        super(AbstractOptimizer, self).__init__(name, **kwargs)
        self._set_hyper('learning_rate', kwargs.get('lr', learning_rate))

    def _create_slots(self, var_list):
        pass

    def _resource_apply_dense(self, grad, var):
        raise NotImplementedError

    def _resource_apply_sparse(self, grad, var, indices):
        raise NotImplementedError

    def get_config(self):
        base_config = super(AbstractOptimizer, self).get_config()
        base_config.update({
            'learning_rate': self._serialize_hyperparameter('learning_rate'),
        })
        return base_config
