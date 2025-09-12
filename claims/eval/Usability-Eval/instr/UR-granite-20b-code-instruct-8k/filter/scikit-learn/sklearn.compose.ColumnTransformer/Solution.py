
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

column_transformer = ColumnTransformer(
    transformers=[
        ('scaler', StandardScaler(), [0, 1]),
        ('pca', PCA(n_components=2), [2, 3])
    ]
)
