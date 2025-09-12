
import pandas as pd
from sklearn.decomposition import PCA

# Load data
data = pd.read_csv("data.csv")

# Apply PCA to reduce dimensionality
pca = PCA(n_components=0.9)
pca_data = pca.fit_transform(data)

print(pca_data.shape)
