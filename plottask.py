# Plottask.py
# This Program displays a plot of the functions: f(x)=x, g(x)=x2 and h(x)=x3 in the range [0, 4] on the one set of axes.
# Author: Katie Mc Donald

# Importing Modules
import numpy as np
import matplotlib.pyplot as plt

# f(x)=x
xpoints = np.array(range(0,4))
ypoints = xpoints
# Plotting x, y, label, color as RGB code, linewidth, linestyle, marker, markersize
plt.plot(xpoints, ypoints, label='f(x)=x', color='#94E2F2', lw=2, ls='-', marker='o', ms=5)
# g(x)=x2
# Plotting g, label, color as RGB code, linewidth, linestyle, marker, markersize
plt.plot(xpoints, xpoints * 2, label='g(x)=x2', color="#635BD5", lw=2, ls='-', marker='o', ms=5)
# h(x)=x3
# Plotting h, label, color as RGB code, linewidth, linestyle, marker, markersize
plt.plot(xpoints, xpoints*3, label='h(x)=x3', color='#FF8C00', lw=2, ls='-', marker='o', ms=5)

# X-axis label, color
plt.xlabel('X Axis', color='black')
# Y axis label, color
plt.ylabel('Y Axis', color='black')
# Plot title, color
plt.title('Weekly Task 08 - Plot Task', color='black')
# Adding a legend
plt.legend()
# Adding a grid to the plot, linewidth, color, linestyle
plt.grid( color='green', lw=0.15, ls="--")
# Adding ticks to each axes 
plt.xticks([0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5])
plt.yticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9,10])

# Shows graph when program runs. Using show() as task criteria said to display not save
plt.show() 