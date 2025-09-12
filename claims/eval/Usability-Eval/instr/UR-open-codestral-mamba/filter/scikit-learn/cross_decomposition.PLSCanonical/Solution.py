from sklearn.cross_decomposition import PLSRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Assuming we have X as independent variables and y as dependent variable
# And we have already split our dataset into train and test dataset

# Create a Partial Least Squares regressor: pls
pls = PLSRegression()

# Fit the regressor to the data
pls.fit(X_train, y_train)

# Make predictions
y_pred = pls.predict(X_test)
# Calculate Root Mean Squared Error
rmse = np.sqrt(mean_squared_error(y_test, y_pred))

print('Root Mean Squared Error (RMSE):', rmse)
