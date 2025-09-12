import pandas as pd

# Sample data creation
data = {
    'Fruit': ['Apples', 'Oranges', 'Bananas'],
    'Color': ['Red', 'Orange', 'Yellow'],
    'Count': [100, 200, 300]
}
df = pd.DataFrame(data)

# Generate LaTeX styled representation
latex = df.style
latex.set_table_styles(['{}.set_font_size(12)',
                        '{}.set_font_weight("bold")'])

# Output to LaTeX format
latex.render()

# To save to a string
latex_str = latex.get_value()

# Alternatively, you can write to a file
with open('styled_table.tex', 'w') as f:
    f.write(latex.render())
