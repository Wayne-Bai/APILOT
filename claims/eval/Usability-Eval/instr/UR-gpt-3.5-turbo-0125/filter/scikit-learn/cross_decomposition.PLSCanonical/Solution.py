
from sklearn.cross_decomposition import PLSRegression
from sklearn.preprocessing import StandardScaler

# Create a Partial Least Squares (PLS) transformer
pls_transformer = PLSRegression(n_components=2)

# Create a Partial Least Squares (PLS) regressor
pls_regressor = PLSRegression(n_components=2)

# Optionally, you can also include a standard scaler
scaler = StandardScaler()
pls_transformer = make_pipeline(scaler, pls_transformer)
pls_regressor = make_pipeline(scaler, pls_regressor)
