import pandas as pd

# Creating example DataFrame
df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6]
})

# Adding a string suffix to column labels
df.columns = [f"{col}_suffix" for col in df.columns]

print(df)
