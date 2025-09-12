
import sklearn

class SubEstimatorDecorator:
    def __init__(self, estimator):
        self.estimator = estimator
    
    def __call__(self, *args, **kwargs):
        # Delegate the method call to the sub-estimator
        return self.estimator(*args, **kwargs)
