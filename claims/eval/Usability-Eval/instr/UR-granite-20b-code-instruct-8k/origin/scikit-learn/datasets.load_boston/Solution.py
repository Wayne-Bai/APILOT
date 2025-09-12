from sklearn.datasets import load_boston

boston_data = load_boston()

print(boston_data.keys())

X = boston_data.data
y = boston_data.target

# Optionally split the data into training and testing sets
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

# Now you can use X_train, y_train, X_test, and y_test for further analysis or modeling
