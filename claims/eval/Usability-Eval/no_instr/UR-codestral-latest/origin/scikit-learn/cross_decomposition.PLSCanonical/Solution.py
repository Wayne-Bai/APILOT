from sklearn.model_selection import train_test_split
from sklearn.cross_decomposition import PLSRegression
from sklearn import metrics

# Assume that X is the feature matrix and y is the target vector
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

pls = PLSRegression(n_components=2)

# Fit the PLS model to the training data
pls.fit(X_train, y_train)

# Transform the training and test data
X_train_pls = pls.transform(X_train)
X_test_pls = pls.transform(X_test)

# Use the transformed data to predict the target using the original regressor
y_pred_pls = pls.predict(X_test_pls)

# Calculate the root mean square error of the prediction
rmse = np.sqrt(metrics.mean_squared_error(y_test, y_pred_pls))

print(f'Root Mean Squared Error: {rmse}')
