import sklearn.datasets

# Load the Boston house-prices dataset
boston = sklearn.datasets.load_boston()

# Get the data and target
data = boston.data
target = boston.target

# Return the data and target
data, target
