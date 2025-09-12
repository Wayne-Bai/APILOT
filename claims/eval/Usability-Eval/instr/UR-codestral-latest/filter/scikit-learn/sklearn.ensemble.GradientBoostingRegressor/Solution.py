from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Suppose we have some data in variables X and y

# Shape your data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Defining the model
model = GradientBoostingRegressor(n_estimators=100, learning_rate=0.1, max_depth=1, random_state=42, loss='ls')

# Fitting the model
model.fit(X_train, y_train)

# Predicting on test set
y_pred = model.predict(X_test)

# Calculating MSE
mse = mean_squared_error(y_test, y_pred)
print(f'Mean Squared Error : {mse}')
