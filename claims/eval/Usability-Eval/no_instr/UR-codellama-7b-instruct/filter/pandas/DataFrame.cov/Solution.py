
import pandas as pd

# read csv file into a pandas dataframe
df = pd.read_csv('file.csv')

# compute pairwise covariance of columns using vectorized implementation
cov = pd.Series(df).cov()
