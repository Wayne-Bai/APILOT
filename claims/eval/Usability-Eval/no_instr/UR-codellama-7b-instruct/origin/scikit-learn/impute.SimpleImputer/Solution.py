
from sklearn import datasets
from sklearn.impute import SimpleImputer

# Load the Boston housing dataset
boston = datasets.load_boston()

# Create a copy of the data to prevent modifying the original data
data = boston.copy()

# Drop any non-numeric columns from the data
num_columns = list(data.select_dtypes(include=['int64', 'float64']))
data = data[num_columns]

# Fill in missing values using mean imputation
imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
imputed_data = imputer.fit_transform(data)

# Print the result
print("Imputed data:\n", imputed_data)
