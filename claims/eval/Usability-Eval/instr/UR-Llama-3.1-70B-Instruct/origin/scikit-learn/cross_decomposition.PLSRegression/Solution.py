# Import required libraries
from sklearn.cross_decomposition import PLSSVD
from sklearn import decomposition
from sklearn.preprocessing import StandardScaler
import numpy as np
from sklearn import metrics

# Function to perform PLS regression
def pls_regression(X, y):
    """
    Perform Partial Least Squares regression.
    
    Parameters:
    X (array-like): Features.
    y (array-like): Target.
    
    Returns:
    list: Coefficients.
    """
    
    # Create a PLSSVD object
    pls = PLSSVD(n_components=2)
    
    # Fit the model
    pls.fit(X, y)
    
    # Get the x and y scores
    X_scores = pls.x_scores_
    y_scores = pls.y_scores_
    
    # Transform the data and calculate the coefficients
    X_trans = pls.x_weights_
    coefficients = np.dot(X_trans, pls.y_loadings_.T)
    
    return coefficients

def calculate_coefficients():
    # Generate data
    np.random.seed(0)
    n_samples = 1000
    n_features = 10
    X = np.random.rand(n_samples, n_features)
    coefficients = np.random.rand(n_features)
    y = np.dot(X, coefficients)
    y += np.random.randn(n_samples)
    
    # Create the dataset and standardize the features
    scaler = StandardScaler()
    X = scaler.fit_transform(X)
    
    return X, y


def get_y_pred(X, y, coefficients):
    y_pred = np.dot(X, coefficients)
    
    return y_pred


def get_performance_metrics(y, y_pred):
    mae = metrics.mean_absolute_error(y, y_pred)
    mse = metrics.mean_squared_error(y, y_pred)
    rmse = mse**0.5
    r2_score = metrics.r2_score(y, y_pred)
    print(f"Mean Absolute Error: {mae}")
    print(f"Mean Squared Error: {mse}")
    print(f"Root Mean Squared Error: {rmse}")
    print(f"R-Squared Score: {r2_score}")


if __name__ == "__main__":
    X, y = calculate_coefficients()
    coefficients = pls_regression(X, y)
    y_pred = get_y_pred(X, y, coefficients)
    get_performance_metrics(y, y_pred)
