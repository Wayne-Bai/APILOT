# Import necessary libraries
import seaborn as sns
import matplotlib.pyplot as plt

# Load the tips dataset
tips = sns.load_dataset("tips")

# Show point estimates and errors using lines with markers
plt.figure(figsize=(10,6))
sns.lineplot(data=tips, x="day", y="total_bill", estimator=np.mean, err_style="band", ci=68)
plt.title('Point estimates and errors using lines with markers')
plt.show()
