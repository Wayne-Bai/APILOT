# Importing the necessary library
import pandas as pd
import numpy as np

# Creating a DataFrame
data = pd.DataFrame(np.random.randn(5, 3), columns=['A', 'B', 'C'])
data['A'] = data['A'].apply(lambda x: round(x, 2))
data['B'] = data['B'].apply(lambda x: round(x, 2))
data['C'] = data['C'].apply(lambda x: round(x, 2))

# Writing Styler to a LaTeX file
def to_latex(df):
    styler = df.style \
       .format(na_rep='-', precision=2) \
       .set_caption('Table caption') \
       .set_properties(**{'background-color': '#f7f7f7', 
                           'color': 'black', 
                           'border-color': 'black'}) \
       .set_table_styles([{'selector': 'th', 
                            'props': [('font-size', '10pt'), 
                                      ('text-align', 'center')]}])

    latex = styler.to_latex(convert_csv=True, position=None)

    with open('output.tex', 'w') as f:
        f.write(latex)

# Using the function
to_latex(data)
