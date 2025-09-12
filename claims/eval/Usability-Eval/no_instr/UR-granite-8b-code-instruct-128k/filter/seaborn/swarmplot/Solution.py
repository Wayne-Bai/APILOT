
import seaborn as sns

# Assuming you have two categorical variables 'cat_var1' and 'cat_var2',
# and a continuous variable 'cont_var' in your DataFrame 'df'.

sns.scatterplot(data=df, x='cat_var1', y='cat_var2', size='cont_var')
