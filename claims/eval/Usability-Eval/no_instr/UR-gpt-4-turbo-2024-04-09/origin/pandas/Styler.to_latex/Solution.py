import pandas as pd

# Create a sample dataframe
df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 8, 9]
})

# Use Styler to format the dataframe for LaTeX
styler = df.style.to_latex()

# Write the LaTeX formatted data to a file
with open("output.tex", "w") as file:
    file.write(styler)
