import numpy as np
from sklearn.linear_model import LassoLars
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import mean_squared_error

# Generate some data
np.random.seed(0)
n_samples, n_features = 50, 100
X = np.random.normal(size=(n_samples, n_features))
y = np.random.normal(size=n_samples)

# Define the parameter grid for cross validation
param_grid = {
    'alpha': np.logspace(-4, 0, 50),
   'max_iter': [1000]
}

# Initialize LassoLars model and fit with GridSearchCV for model selection
lasso_model = LassoLars()
grid_search = GridSearchCV(lasso_model, param_grid, cv=5, scoring='neg_mean_squared_error')
grid_search.fit(X, y)

# Get the best alpha value based on CV
best_alpha = grid_search.best_params_['alpha']

# Create a new LassoLars model with the best alpha value and fit to the data
best_model = LassoLars(alpha=best_alpha)
best_model.fit(X, y)

# Predict y using the best model
y_pred = best_model.predict(X)

# Calculate the MSE of the best model
mse = mean_squared_error(y, y_pred)
print(f'MSE of the best model: {mse}')

# For BIC or AIC manual model selection you can use below approach
def calculate_bic(n, mse, df):
    return n * np.log(mse) + df * np.log(n)

def calculate_aic(n, mse, df):
    return n * np.log(mse) + 2 * df

n = X.shape[0]
for alpha in np.logspace(-4, 0, 50):
    model = LassoLars(alpha=alpha)
    model.fit(X, y)
    y_pred = model.predict(X)
    mse_value = mean_squared_error(y, y_pred)
    df = np.count_nonzero(model.coef_)
    bic = calculate_bic(n, mse_value, df)
    aic = calculate_aic(n, mse_value, df)
    print(f'Alpha: {alpha}, BIC: {bic}, AIC: {aic}')
