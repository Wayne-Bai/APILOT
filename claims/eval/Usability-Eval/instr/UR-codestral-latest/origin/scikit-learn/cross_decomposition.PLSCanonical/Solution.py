# Import required modules
from sklearn.cross_decomposition import PLSRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Define your independent variables (X) and dependent variable (y)
# Here, use your actual data
# X, y = ...

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a PLS regression object
pls2 = PLSRegression(n_components=2)

# Fit the model to the training data
pls2.fit(X_train, y_train)

# Make predictions on the test set
y_pred = pls2.predict(X_test)

# Calculate the mean squared error to evaluate performance
mse = mean_squared_error(y_test, y_pred)
print('Mean Squared Error:', mse)
