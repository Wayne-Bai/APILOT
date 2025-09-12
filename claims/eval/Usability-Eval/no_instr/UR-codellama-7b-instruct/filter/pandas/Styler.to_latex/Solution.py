
import pandas as pd

# create a styler object from a dataframe
styler = pd.Styler(df)

# write the styled dataframe to a file in LaTeX format
styler.to_latex('styled_df.tex', float_format='{:.2f}')
