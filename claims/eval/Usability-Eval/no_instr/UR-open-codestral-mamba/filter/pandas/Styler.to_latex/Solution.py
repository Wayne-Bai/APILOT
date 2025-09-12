# Importing the pandas library
import pandas as pd

# Creating a sample DataFrame
data = {
    'Name': ['John', 'Jane', 'Mike'],
    'Age': [25, 30, 35],
    'Gender': ['Male', 'Female', 'Male']
}
df = pd.DataFrame(data)

# Writing DataFrame to a LaTeX file
df.to_latex('sample.tex')

# Printing a success message
print("LaTeX format data has been successfully saved to the file 'sample.tex'")
