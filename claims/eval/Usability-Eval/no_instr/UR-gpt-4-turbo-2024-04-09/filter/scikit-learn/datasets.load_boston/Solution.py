import sklearn
from sklearn.datasets import load_boston

# Load the Boston housing dataset
boston = load_boston()
X, y = boston.data, boston.target
