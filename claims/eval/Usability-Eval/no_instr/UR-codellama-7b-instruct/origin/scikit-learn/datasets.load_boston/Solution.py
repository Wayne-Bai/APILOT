
import pandas as pd
from sklearn import datasets

# Load Boston Housing Prices Dataset
boston_housing = datasets.load_boston()

# Return dataset as Pandas DataFrame
boston_df = pd.DataFrame(boston_housing.data, columns=boston_housing.feature_names)
boston_df['PRICE'] = boston_housing.target

return boston_df
