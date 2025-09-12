
from sklearn.linear_model import LinearRegression
from sklearn.decomposition import PLSRegression
from sklearn.pipeline import make_pipeline

# Create the PLS transformer
pls = PLSRegression(n_components=5)

# Create the linear regression model
lr = LinearRegression()

# Create the pipeline that combines the PLS transformer and the linear regression model
pipe = make_pipeline(pls, lr)
