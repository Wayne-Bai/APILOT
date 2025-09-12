
import pandas as pd

# read the csv file into a dataframe
df = pd.read_csv("data.csv")

# compute the pairwise covariance matrix
cov_matrix = df.corr(method="pearson", min_periods=1)

# exclude rows with missing values
df = df.dropna()

# compute the pairwise covariance of columns
cov = pd.DataFrame(columns=[])
for i in range(len(df.columns)):
    for j in range(i+1, len(df.columns)):
        cov[f"{df.columns[i]}-{df.columns[j]}"] = df[df.columns[i]].corr(df[df.columns[j]])

# output the results
print(cov)
