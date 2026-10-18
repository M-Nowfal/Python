# PROGRAM 7 – Program to demonstrate Data visualization.

import matplotlib.pyplot as plt
import numpy as np

plt.style.use('ggplot')

np.random.seed(42)

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'June']

Sales = [120, 145, 130, 170, 210, 195]

Categories = ['Apparel', 'Electronics', 'Home', 'Grocery', 'Toys']

Revenue = [25000, 42000, 18000, 30000, 12500]

heights = np.random.normal(170, 10, 100)

weights = heights * 0.4 + np.random.normal(0, 5, 100)

Scores = np.random.normal(70, 15, 500)

group_a = np.random.normal(60, 10, 50)

group_b = np.random.normal(75, 12, 50)

group_c = np.random.normal(65, 8, 50)

fig, axes = plt.subplots(3, 2, figsize=(14, 18))

fig.suptitle(
  'Data Visualization Techniques (Matplotlib)',
  fontsize=18,
  fontweight='bold'
)

axes[0, 0].plot(
  months,
  Sales,
  marker='o',
  color='tab:blue',
  linewidth=2
)

axes[0, 0].set_title('Line Chart: Monthly Sales Trend')

axes[0, 0].set_xlabel('Months')

axes[0, 0].set_ylabel('Sales (Units)')

axes[0, 1].bar(
  Categories,
  Revenue,
  color='tab:orange'
)

axes[0, 1].set_title('Revenue by Category')

axes[0, 1].set_xlabel('Categories')

axes[0, 1].set_ylabel('Revenue ($)')

scatter = axes[1, 0].scatter(
  heights,
  weights,
  c='tab:green',
  alpha=0.7,
  edgecolors='none'
)

axes[1, 0].set_xlabel('Height (cm)')

axes[1, 0].set_ylabel('Weight (kg)')

fig.colorbar(
  scatter,
  ax=axes[1, 0],
  label='Weight Scale'
)


axes[1, 1].hist(
  Scores,
  bins=20,
  color='tab:purple',
  edgecolor='black',
  alpha=0.7
)

axes[1, 1].set_xlabel('Scores')

axes[1, 1].set_ylabel('Frequency')

axes[2, 0].boxplot(
  [group_a, group_b, group_c],
  label=['Group A', 'Group B', 'Group C'],
  patch_artist=True,
  boxprops=dict(facecolor='lightblue', color='blue')
)

axes[2, 0].set_xlabel('Groups')

axes[2, 0].set_ylabel('Performance Metric')

axes[2, 0].grid(axis='y')

axes[2, 1].axis('off')

plt.tight_layout()

plt.show()
