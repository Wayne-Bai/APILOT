import seaborn as sns
import matplotlib.pyplot as plt

# Load data
tips = sns.load_dataset("tips")

# Draw strip plot with jitter
sns.stripplot(x="day", y="total_bill", hue="smoker", data=tips, jitter=0.3)
plt.title("Strip Plot with Jitter")
plt.show()
