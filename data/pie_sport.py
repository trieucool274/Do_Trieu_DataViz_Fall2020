import matplotlib.pyplot as plt
import numpy as np
hfont = { 'fontname': 'Times New Roman' }


y = np.array([3, 22, 50, 351, 124, 40 ])
mylabels = [ "Biathlon", "Bobsleigh", "Curling", "Ice Hockey", "Skating", "Skiing" ]
myexplode = [0.2, 0,0.1,0.1,0.1,0.1]
plt.pie(y, labels = mylabels, startangle = 90, autopct='%1.1f%%',
        shadow=True, explode=myexplode )

plt.title("Type of sports", pad=20, **hfont)
plt.show()