import seaborn as sns
import matplotlib.pyplot as plt

# Assuming you have a DataFrame df with columns 'value' and 'error'
sns.barplot(x=df['value'], y=df['error'], orient='v', color='skyblue')
plt.errorbar(df['value'], df['error'], xerr=df['error'], fmt='o', color='black')
plt.show()
