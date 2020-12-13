
import numpy as np
import matplotlib.pyplot as plt

# data to plot
n_groups = 3
Canada = (220, 35, 30 )
USA = (25, 32, 34 )

# create plot
fig, ax = plt.subplots()
index = np.arange(n_groups)
bar_width = 0.35
opacity = 0.8

rects1 = plt.bar(index, Canada, bar_width,
alpha=opacity,
color='yellow',
label='Canada')

rects2 = plt.bar(index + bar_width, USA, bar_width,
alpha=opacity,
color='black',
label='USA')

plt.ylabel('Medals won')
plt.title('Number of Ice Hockey medals earned by Canada and USA')
plt.xticks(index + bar_width, ('Gold', 'Silver', 'Bronze'))
plt.legend()

plt.tight_layout()

plt.show()