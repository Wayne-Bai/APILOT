
from sklearn.decomposition import PLSRegressor
from sklearn.decomposition import PLSComposedTransformer

# Load the dataset
X = ... # feature data
y = ... # target data

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the PLS regressor
pls = PLSRegressor(n_components=3)

# Fit the PLS model to the training data
pls.fit(X_train, y_train)

# Predict on the testing data
y_pred = pls.predict(X_test)

# Evaluate the performance of the model
r2 = r2_score(y_test, y_pred)
print(f"R-squared: {r2}")

# Initialize the PLS composed transformer
pls_ct = PLSComposedTransformer(n_components=3)

# Fit the PLS composed transformer to the training data
pls_ct.fit(X_train, y_train)

# Predict on the testing data
y_pred = pls_ct.predict(X_test)

# Evaluate the performance of the model
r2 = r2_score(y_test, y_pred)
print(f"R-squared: {r2}")
