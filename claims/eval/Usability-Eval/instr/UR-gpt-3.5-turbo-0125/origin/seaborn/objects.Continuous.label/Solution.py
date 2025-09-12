
import seaborn as sns

# Set the font size of tick labels in x-axis
sns.set_context("talk")
sns.set_style("whitegrid")
sns.set(font_scale=1.5)

# Set the font size of tick labels in y-axis
plt.figure(figsize=(8,6))
sns.barplot(x='day', y='total_bill', data=tips)
plt.yticks(fontsize=12)

plt.show()
