import matplotlib.pyplot as plt

hfont = { 'fontname': 'Times New Roman' }

labels = 'Gold', 'Silver', 'Bronze', 
sizes = [315, 203, 107]
explode = (0, 0.1, 0,)  # only "explode" the 2nd slice (i.e. 'Silver') 
mycolors = ["Gold", "Grey", "Brown"]

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, colors=mycolors, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title("Type of Medals earned - 90 Years", pad=20, **hfont)

plt.show()

import matplotlib
matplotlib.axes.Axes.pie
matplotlib.pyplot.pie
