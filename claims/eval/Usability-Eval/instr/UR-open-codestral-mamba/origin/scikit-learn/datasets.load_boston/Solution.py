from sklearn.datasets import load_boston

# load the boston house-prices dataset
boston_dataset = load_boston()

# Print the names of the 13 features
print("Features:", boston_dataset.feature_names)

# Print the label type of housing price
print("Label:", boston_dataset.target)
