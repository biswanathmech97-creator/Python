import matplotlib.pyplot as plt
import numpy as np

# Generate random data: 100 points for 3 different distributions
np.random.seed(10)
data = [np.random.normal(0, std, 200) for std in range(2, 12)]

fig, ax = plt.subplots()

# Create the violin plot
# showmedians=True adds a line for the median
vplot = ax.violinplot(data, showmeans=False, showmedians=True, showextrema=True)

# Customizing colors (optional)
for body in vplot['bodies']:
    body.set_facecolor('skyblue')
    body.set_alpha(0.7)

ax.set_title('Basic Violin Plot')
ax.set_xticks([1, 2, 3])
ax.set_xticklabels(['Group A', 'Group B', 'Group C'])
ax.set_ylabel('Values')

plt.show()
