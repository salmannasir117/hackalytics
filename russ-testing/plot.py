# Libraries
import pandas as pandas
import mpld3 as plt

fig, ax = plt.subplots(subplot_kw=dict(axisbg='#EEEEEE'))

ax.grid(color='white', linestyle='solid')

ax.set_title("Plot Title", size=30)



mpld3.show()