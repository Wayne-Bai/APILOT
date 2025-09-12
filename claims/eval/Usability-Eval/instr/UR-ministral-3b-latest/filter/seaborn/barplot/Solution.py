import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

tips = sns.load_dataset("tips")
mean_var = tips.groupby("day", as_index=False).mean()
mean_var = mean_var.sort_values(["day"])

plt.figure(figsize=(8, 6))
sns.barplot(data=mean_var, x="day", y="total_bill", yerr="total_bill_err")
plt.show()
