
import pandas as pd

# load data
df = pd.read_csv("data.csv")

# compute pairwise correlation matrix
corr_mat = df.corr().values

# exclude NA/null values
mask = ~(np.isnan(corr_mat) | np.isinf(corr_mat))
corr_mat_clean = corr_mat[mask]

# display result
print(corr_mat_clean)
