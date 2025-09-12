import seaborn as sns
import matplotlib.pyplot as plt

# Assuming you have a DataFrame df with columns 'column1' and 'column2'
# Replace 'column1' and 'column2' with your actual column names

# Create a boxplot with enhanced features
sns.boxplot(x="column1", y="column2", data=df, width=0.5, whis=[5, 95])

# Add title and labels
plt.title('Enhanced Box Plot')
plt.xlabel('Column1')
plt.ylabel('Column2')

# Display the plot
plt.show()
