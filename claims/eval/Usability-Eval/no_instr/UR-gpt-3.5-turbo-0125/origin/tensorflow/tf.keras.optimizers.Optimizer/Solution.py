
import tensorflow as tf

class AbstractOptimizer:
    def __init__(self):
        pass
        
    def minimize(self, loss, var_list):
        raise NotImplementedError("minimize method must be implemented in subclass")        
