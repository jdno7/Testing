# import tkinter
import matplotlib
# matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

x_vals = [1,2,3,4]
y_vals = [1,2,3,4]

plt.plot(x_vals,y_vals)

plt.savefig('plot.png', dpi=300, bbox_inches='tight')

plt.show()

