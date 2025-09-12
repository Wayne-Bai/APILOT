from sklearn.cross_decomposition import PLSRegression
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.datasets import make_regression

# Generate some regression data
X, y = make_regression(n_samples=1000, n_features=10, noise=0.1)

# Center and scale the data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Create a PLS regression model
pls_model = make_pipeline(scaler, PLSRegression(n_components=2))

# Fit the model to the data
pls_model.fit(X_scaled, y)

# Predict the target variable for new data
X_new, _ = make_regression(n_samples=100, n_features=10, noise=0.1)
X_new_scaled = scaler.transform(X_new)
y_pred = pls_model.predict(X_new_scaled)
