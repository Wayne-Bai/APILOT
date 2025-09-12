import pandas as pd

# Create a DataFrame
df = pd.DataFrame({
    'First Name': ['John', 'Anna', 'Peter', 'Linda'],
    'Last Name': ['Doe', 'Smith', 'Johnson', 'Anderson']
})

# Create a Styler object
styler = df.style

# Add some background color and styling
styler.background_gradient(cmap='coolwarm', subset=['First Name'])

# Styler to LaTeX
latex_data = styler.to_latex(multirow=False)

# Write LaTeX data to a buffer or a file
buffer = latex_data.encode('utf-8')
latex_file_name = "output.tex"
with open(latex_file_name, "w", encoding='utf-8') as file:
    file.write(latex_data)

# For writing to a string
latex_string = latex_data
print(latex_string)
