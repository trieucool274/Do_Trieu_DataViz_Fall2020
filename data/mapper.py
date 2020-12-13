import matplotlib.pyplot as plt 

hfont = { 'fontname': 'Times New Roman' }

# plot / chart world population for the past 115 years

years = [1924, 1928, 1932, 1936, 1948, 1952, 1956, 1960, 1964, 1968, 1972, 1976, 1980, 1984, 1988, 1992, 1994, 1998, 2002, 2006, 2010, 2014 ]

pops = [9, 12, 20, 13, 20, 17, 20, 21, 7, 20, 1, 3, 2, 4, 6, 37, 40, 49, 75, 68, 91, 90]


plt.plot(years, pops, color=(150/255, 200/255, 200/255), linewidth=4.0)

#add some labels 
plt.ylabel("Medals earned each year")
plt.xlabel("Medals Growth by Year")
plt.title("Total Medals earned - 90 Years", pad=20, **hfont)


plt.show()
