from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.linear_model import LassoLars
from sklearn.pipeline import make_pipeline

# Creating a pipeline with StandardScaler, PCA, and LassoLars
model = make_pipeline(
    StandardScaler(),
    PCA(n_components=2),
    LassoLars()
)

# Initializing and fitting the model
model.fit(X_train, y_train)
