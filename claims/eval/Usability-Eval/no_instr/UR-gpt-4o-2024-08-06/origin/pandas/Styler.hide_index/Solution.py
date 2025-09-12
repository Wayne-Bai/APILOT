import pandas as pd

# Sample DataFrame
data = {
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 8, 9]
}

df = pd.DataFrame(data)

# To hide the entire index from the DataFrame rendering
df_styles = df.style.hide(axis='index')

# Display the DataFrame with hidden index in a Jupyter environment or similar
df_styles
