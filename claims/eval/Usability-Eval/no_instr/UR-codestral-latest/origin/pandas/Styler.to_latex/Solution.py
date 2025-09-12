import pandas as pd

# create a DataFrame
data = {'Name': ['Tom', 'Nick', 'John', 'Peter'],
        'Age': [20, 21, 19, 18]}
df = pd.DataFrame(data)

# applying the dataframe styler
styled_df = df.style.hide_index()

# export the styler to a LaTeX file
styled_df.to_latex('styled_data.tex')
