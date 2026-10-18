import matplotlib.pyplot as plt
import numpy as np

plt.style.use('ggplot')
np.random.seed(42)

fig, axes = plt.subplots(3, 2, figsize=(30, 40))

months = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'July', 'Aug')
sales = [120, 140, 135, 125, 160, 170, 190, 185]

category = ['Electronics', 'Home', 'Grocery', 'Toys']
revenue = [42000, 34000, 56000, 10000]

heights = np.random.normal(70, 10, 100)
weights = heights * 0.4 + np.random.normal(0, 10, 100)

scores = np.random.normal(70, 15, 500)

garoup_a = np.random.normal(20, 0, 50)
garoup_b = np.random.normal(10, 20, 50)
garoup_c = np.random.normal(15, 5, 50)

def set_labels(ax, title, x_label, y_label):
  ax.set_title(title)
  ax.set_xlabel(x_label,  fontweight='bold', color='black')
  ax.set_ylabel(y_label, fontweight='bold', color='black')
  
axes[0, 0].plot(months, sales, color='blue')
set_labels(axes[0, 0], "Monthly Sales", "Month", "Sales")

axes[0, 1].bar(category, revenue)
set_labels(axes[0, 1], "Catgory Revenue", "Category", "Revenue")

scatter = axes[1, 0].scatter(heights, weights, cmap='viridis')
fig.colorbar(
  scatter,
  ax=axes[1, 0],
  label='Weight Scale'
)
set_labels(axes[1, 0], "Heights & Weights", "Heights", "Weights")

axes[1, 1].hist(scores, bins=20, color='purple', edgecolor='black')
set_labels(axes[1, 1], "Histogram", "Scores", "Level")

axes[2, 0].boxplot([garoup_a, garoup_b, garoup_c], label=['Group_A', 'Group_B', 'Group_C'])

plt.show()