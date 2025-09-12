import pandas as pd

# Create a DataFrame
data = [['Country', 'City', 'Population'],
        ['USA', 'New York', 8.4],
        ['USA', 'Chicago', 2.7],
        ['India', 'Mumbai', 12.4],
        ['India', 'Delhi', 10.9]]

df = pd.DataFrame(data[1:], columns=data[0])

# Use the to_latex method
latex_output = df.to_latex(index=False)

# Print the LaTeX output
print(latex_output)

# Write the LaTeX output to a file
with open('output.tex', 'w') as f:
    f.write(latex_output)
