import pandas as pd

# Sample DataFrame
df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 8, 9]
})

# Hide column headers
df_styled = df.style.hide_index()  # If you want to hide only the index

# Display the styled DataFrame
print(df_styled)
