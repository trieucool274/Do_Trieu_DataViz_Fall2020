import numpy as np
import matplotlib.pyplot as plt

# data to plot
n_groups = 3
means_men = (192, 128, 66)
means_women = (123, 75, 41)

# create plot
fig, ax = plt.subplots()
index = np.arange(n_groups)
bar_width = 0.35
opacity = 0.8

rects1 = plt.bar(index, means_men, bar_width,
alpha=opacity,
color='red',
label='Men')

rects2 = plt.bar(index + bar_width, means_women, bar_width,
alpha=opacity,
color='blue',
label='Women')

plt.ylabel('Medals won')
plt.title('Number of medals earned by Men and Women')
plt.xticks(index + bar_width, ('Gold', 'Silver', 'Bronze'))
plt.legend()

plt.tight_layout()
plt.show()
