import pandas as pd

# Assuming the data is stored in a variable called 'data'
data = pd.DataFrame({
   'A': [1, 2, 3],
   'B': [4, 5, 6],
   'C': [7, 8, 9]
})

# Hide the entire index
data.style.hide_index()

# Hide the entire column headers
data.style.hide_columns()
