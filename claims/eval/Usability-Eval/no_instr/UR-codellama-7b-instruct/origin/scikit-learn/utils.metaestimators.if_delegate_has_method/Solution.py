
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import numpy as np

def sub_estimator(method):
    def wrapper(self, *args, **kwargs):
        if not isinstance(self, PCA) and not isinstance(self, StandardScaler):
            raise TypeError("Sub-estimators should be instances of PCA or StandardScaler")
        return method(self, *args, **kwargs)
    return wrapper
