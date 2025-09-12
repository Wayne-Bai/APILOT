import seaborn as sns
import matplotlib.pyplot as plt

# Sample data
data = sns.load_dataset("tips")

# Create a basic seaborn plot
sns.set(style="whitegrid")
ax = sns.scatterplot(x="total_bill", y="tip", data=data)

# Configure the appearance of tick labels
ax.tick_params(axis='x', labelsize=14, labelcolor='red', rotation=45)  # X-axis tick label configuration
ax.tick_params(axis='y', labelsize=12, labelcolor='blue')             # Y-axis tick label configuration

# Configure the appearance of legend tick labels 
legend = ax.legend()
for text in legend.get_texts():
    text.set_color("purple")
    text.set_fontsize(10)

# Show plot
plt.show()
