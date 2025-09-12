import pandas as pd

# Assuming df is your DataFrame
# Create a mask for non-null values
non_null_mask = ~df.isnull()

# Compute pairwise covariances by only considering non-null values
covariance_matrix = non_null_mask.astype(int).mul(df.cov().values)

# Costom fill None with the actual covariance values because multiply mask Replace NA with 0.0
covariance_matrix = pd.DataFrame(covariance_matrix.values, index=df.columns, columns=df.columns)
