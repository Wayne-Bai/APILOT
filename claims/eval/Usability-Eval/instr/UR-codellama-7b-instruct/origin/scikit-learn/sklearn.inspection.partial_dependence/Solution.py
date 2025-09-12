
from sklearn import datasets
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

# Load Boston dataset
boston = datasets.load_boston()
X = boston.data
y = boston.target

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a random forest regressor object with 100 trees
rf = RandomForestRegressor(n_estimators=100, random_state=42)

# Fit the model to the training data
rf.fit(X_train, y_train)

# Get partial dependence for feature 3
partial_dependence = rf.partial_dependence(feature_index=3)
print("Partial dependence of feature 3:", partial_dependence)
