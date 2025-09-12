from sklearn.datasets import load_boston

# Load the boston house-prices dataset
boston = load_boston()

# Return the data and target
data = boston.data
target = boston.target
