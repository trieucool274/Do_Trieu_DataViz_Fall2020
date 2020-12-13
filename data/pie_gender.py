import matplotlib.pyplot as plt
import numpy as np
hfont = { 'fontname': 'Times New Roman' }

y = np.array([386, 239 ])
mylabels = ["Men", "Women"]

myexplode = [0.2, 0]

mycolors = ["red", "blue" ]

plt.pie(y, labels = mylabels, explode=myexplode, colors=mycolors , autopct='%1.1f%%', shadow = True)
plt.legend(title = "Genders" )
plt.title("Male and Female Medialists", pad=20, **hfont)

plt.show()