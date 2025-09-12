
import seaborn as sns
import matplotlib.pyplot as plt

sns.set(style="whitegrid")
tips = sns.load_dataset("tips")

plt.figure(figsize=(12, 6))
sns.boxplot(x="day", y="total_bill", hue="sex", data=tips, palette="muted", fliersize=5)

plt.legend(title='Gender', loc='upper right')
plt.title('Boxplot of Total Bill by Day and Gender')
plt.show()
